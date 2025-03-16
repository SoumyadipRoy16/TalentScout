import os
import time
import re
import streamlit as st
from typing import Dict, List, Optional
import groq
from dotenv import load_dotenv
from utils.constants import STATES, EXIT_KEYWORDS, EMAIL_REGEX, PHONE_REGEX, MAX_TECH_QUESTIONS
from utils.session_state import update_candidate_info, set_conversation_state, get_conversation_state
from utils.prompt_templates import (
    SYSTEM_PROMPT,
    get_information_extraction_prompt,
    get_technical_questions_prompt
)

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

def check_exit_keywords(message: str) -> bool:
    """Check if the message contains exit keywords.
    
    Args:
        message: User message to check
        
    Returns:
        True if exit keywords found, False otherwise
    """
    return any(keyword in message.lower() for keyword in EXIT_KEYWORDS)

def extract_information(user_message: str, info_type: str) -> Optional[str]:
    """Extract specific information from user message using LLM.
    
    Args:
        user_message: User message to extract information from
        info_type: Type of information to extract
        
    Returns:
        Extracted information or None if not found
    """
    prompt = get_information_extraction_prompt(user_message, info_type)
    
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=100
        )
        
        extracted_info = response.choices[0].message.content.strip()
        
        # Handle specific validation for different info types
        if info_type == "email" and not re.match(EMAIL_REGEX, extracted_info):
            return None
        
        if info_type == "phone" and not re.match(PHONE_REGEX, extracted_info):
            return None
            
        return extracted_info
    except Exception as e:
        print(f"Error extracting information: {e}")
        return None

def generate_technical_questions(tech_stack: str) -> List[str]:
    """Generate technical questions based on the candidate's tech stack.
    
    Args:
        tech_stack: Candidate's technology stack
        
    Returns:
        List of technical questions
    """
    prompt = get_technical_questions_prompt(tech_stack)
    
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        
        questions_text = response.choices[0].message.content.strip()
        
        # Extract individual questions (assuming they're numbered)
        questions = []
        for line in questions_text.split('\n'):
            line = line.strip()
            if re.match(r'^[\d\.\)\-]+', line) and len(line) > 5:
                # Remove numbering and trim
                clean_question = re.sub(r'^[\d\.\)\-]+\s*', '', line).strip()
                if clean_question:
                    questions.append(clean_question)
        
        # Limit to MAX_TECH_QUESTIONS
        return questions[:MAX_TECH_QUESTIONS]
    except Exception as e:
        print(f"Error generating technical questions: {e}")
        return ["Error generating questions. Please try again later."]

def get_next_state_response(current_state: str, user_message: str) -> Dict:
    """Determine the next state and appropriate response based on current state and user input.
    
    Args:
        current_state: Current conversation state
        user_message: User's message
        
    Returns:
        Dictionary with next state and response message
    """
    if check_exit_keywords(user_message):
        return {
            "next_state": STATES["conversation_end"],
            "response": "Thank you for your time! Your information has been recorded and our team will be in touch soon. Have a great day!"
        }
    
    # Handle each state in the conversation flow
    if current_state == STATES["collecting_name"]:
        name = extract_information(user_message, "name")
        if name:
            update_candidate_info("full_name", name)
            return {
                "next_state": STATES["collecting_email"],
                "response": f"Nice to meet you, {name}! Could you please provide your email address?"
            }
        else:
            return {
                "next_state": current_state,
                "response": "I didn't catch your full name. Could you please provide it again?"
            }
            
    elif current_state == STATES["collecting_email"]:
        email = extract_information(user_message, "email")
        if email:
            update_candidate_info("email", email)
            return {
                "next_state": STATES["collecting_phone"],
                "response": "Thank you! Now, could you please share your phone number?"
            }
        else:
            return {
                "next_state": current_state,
                "response": "That doesn't look like a valid email address. Could you please provide it in the format example@domain.com?"
            }
            
    elif current_state == STATES["collecting_phone"]:
        phone = extract_information(user_message, "phone")
        if phone:
            update_candidate_info("phone", phone)
            return {
                "next_state": STATES["collecting_experience"],
                "response": "Great! How many years of experience do you have in your field?"
            }
        else:
            return {
                "next_state": current_state,
                "response": "I couldn't recognize that as a valid phone number. Could you please provide it again?"
            }
            
    elif current_state == STATES["collecting_experience"]:
        experience = extract_information(user_message, "experience")
        if experience:
            update_candidate_info("experience", experience)
            return {
                "next_state": STATES["collecting_position"],
                "response": "Thank you! What position(s) are you interested in applying for?"
            }
        else:
            return {
                "next_state": current_state,
                "response": "I didn't catch your years of experience. Could you please provide it as a number or range?"
            }
            
    elif current_state == STATES["collecting_position"]:
        position = extract_information(user_message, "position")
        if position:
            update_candidate_info("desired_position", position)
            return {
                "next_state": STATES["collecting_location"],
                "response": "Excellent! Where are you currently located?"
            }
        else:
            return {
                "next_state": current_state,
                "response": "I didn't understand which position you're interested in. Could you please specify again?"
            }
            
    elif current_state == STATES["collecting_location"]:
        location = extract_information(user_message, "location")
        if location:
            update_candidate_info("location", location)
            return {
                "next_state": STATES["collecting_tech_stack"],
                "response": "Thanks! Now, please list your tech stack - the programming languages, frameworks, databases, and tools you're proficient in."
            }
        else:
            return {
                "next_state": current_state,
                "response": "I didn't catch your location. Could you please specify your city and country?"
            }
            
    elif current_state == STATES["collecting_tech_stack"]:
        tech_stack = extract_information(user_message, "tech_stack")
        if tech_stack:
            update_candidate_info("tech_stack", tech_stack)
            # Generate technical questions based on tech stack
            st.session_state.tech_questions = generate_technical_questions(tech_stack)
            if st.session_state.tech_questions:
                return {
                    "next_state": STATES["asking_tech_questions"],
                    "response": f"Great! Based on your tech stack, I'd like to ask you a few technical questions to assess your proficiency.\n\nFirst question: {st.session_state.tech_questions[0]}"
                }
            else:
                return {
                    "next_state": STATES["conversation_end"],
                    "response": "Thank you for providing your information. Unfortunately, I couldn't generate technical questions at this time. Our team will review your profile and get back to you soon!"
                }
        else:
            return {
                "next_state": current_state,
                "response": "I didn't catch your tech stack. Please list programming languages, frameworks, databases, and tools you're proficient in."
            }
            
    elif current_state == STATES["asking_tech_questions"]:
        # Store the answer to the current question in session state
        current_question = st.session_state.tech_questions[st.session_state.current_question_idx]
        st.session_state.questions_answered += 1
        
        # Move to the next question or end conversation
        st.session_state.current_question_idx += 1
        if st.session_state.current_question_idx < len(st.session_state.tech_questions):
            next_question = st.session_state.tech_questions[st.session_state.current_question_idx]
            return {
                "next_state": STATES["asking_tech_questions"],
                "response": f"Thanks for your answer. Next question: {next_question}"
            }
        else:
            return {
                "next_state": STATES["conversation_end"],
                "response": "Thank you for answering all the technical questions! We've collected all the necessary information for now. Our recruitment team will review your profile and get back to you shortly if there's a good match. Do you have any questions for us?"
            }
            
    elif current_state == STATES["conversation_end"]:
        return {
            "next_state": STATES["conversation_end"],
            "response": "Our team has received your information and will be in touch soon. Have a great day!"
        }
        
    # Fallback for unexpected states
    return {
        "next_state": current_state,
        "response": "I apologize, but I didn't understand that. Could you please try again or rephrase your message?"
    }

def process_user_message(user_message: str, message_placeholder):
    """Process user message and determine the appropriate response.
    
    Args:
        user_message: Message from the user
        message_placeholder: Streamlit placeholder for typing effect
    """
    # Get current conversation state
    current_state = get_conversation_state()
    
    # Get next state and response
    result = get_next_state_response(current_state, user_message)
    next_state = result["next_state"]
    response = result["response"]
    
    # Update conversation state
    set_conversation_state(next_state)
    
    # Display response with typing effect
    display_message_with_typing_effect(response, message_placeholder)
    
    # Store the assistant's response in chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

def display_message_with_typing_effect(message: str, placeholder):
    """Display message with typing effect.
    
    Args:
        message: Message to display
        placeholder: Streamlit placeholder to update
    """
    # Display typing indicator
    placeholder.markdown("▌")
    time.sleep(0.5)
    
    # Split message into words for more natural typing effect
    words = message.split()
    displayed_message = ""
    
    for i, word in enumerate(words):
        displayed_message += word + " "
        placeholder.markdown(displayed_message + "▌")
        # Random typing speed for more natural effect
        delay = min(0.1, 0.02 + (len(word) * 0.005))
        time.sleep(delay)
    
    # Final message without cursor
    placeholder.markdown(message)