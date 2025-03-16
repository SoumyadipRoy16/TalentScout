import streamlit as st
from typing import Dict, List, Any

def initialize_session_state():
    """Initialize or reset the session state variables for the chat application."""
    
    # Initialize messages list if it doesn't exist
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": "Hello! I'm TalentScout's Hiring Assistant. I'll help assess your fit for our technology positions. Could you please tell me your full name to get started?"
            }
        ]
    
    # Initialize candidate information dictionary
    if 'candidate_info' not in st.session_state:
        st.session_state.candidate_info = {
            "full_name": None,
            "email": None,
            "phone": None,
            "experience": None,
            "desired_position": None,
            "location": None,
            "tech_stack": None,
        }
    
    # Initialize conversation state
    if 'conversation_state' not in st.session_state:
        st.session_state.conversation_state = "collecting_name"
    
    # Initialize tech_questions if they don't exist
    if 'tech_questions' not in st.session_state:
        st.session_state.tech_questions = []
    
    # Initialize current question index
    if 'current_question_idx' not in st.session_state:
        st.session_state.current_question_idx = 0
        
    # Initialize answered questions counter
    if 'questions_answered' not in st.session_state:
        st.session_state.questions_answered = 0

def update_candidate_info(field: str, value: Any) -> None:
    """Update a specific field in the candidate information.
    
    Args:
        field: The field to update
        value: The value to set
    """
    st.session_state.candidate_info[field] = value

def set_conversation_state(state: str) -> None:
    """Set the current state of the conversation flow.
    
    Args:
        state: The state to set
    """
    st.session_state.conversation_state = state

def get_conversation_state() -> str:
    """Get the current state of the conversation flow.
    
    Returns:
        Current conversation state
    """
    return st.session_state.conversation_state

def get_candidate_info() -> Dict:
    """Get the current candidate information.
    
    Returns:
        Dictionary containing candidate information
    """
    return st.session_state.candidate_info

def clear_session():
    """Clear the session state and reset to initial values."""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    initialize_session_state()