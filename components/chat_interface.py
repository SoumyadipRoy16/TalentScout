import streamlit as st

def render_chat_interface():
    """Render the chat interface with message history."""
    
    # Create a container for the chat messages
    chat_container = st.container()
    
    # Display chat history
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Add a progress bar for the interview stages
    progress_container = st.container()
    with progress_container:
        # Calculate progress based on conversation state
        progress_percentage = calculate_progress_percentage()
        
        if progress_percentage < 100:
            interview_progress = st.progress(progress_percentage / 100.0)
            st.caption(f"Interview Progress: {progress_percentage}%")
        else:
            interview_progress = st.progress(1.0)
            st.caption("Interview Complete! 100%")
            
        # Add a divider
        st.divider()
        
    # Display candidate information (if available)
    display_candidate_info()

def calculate_progress_percentage() -> int:
    """Calculate the percentage of interview completion.
    
    Returns:
        Progress percentage (0-100)
    """
    # Define the number of steps in our interview process
    # 1. Name, 2. Email, 3. Phone, 4. Experience, 5. Position, 6. Location, 7. Tech Stack, 8. Tech Questions
    total_steps = 8
    current_step = 0
    
    # Count filled fields in candidate_info
    for field, value in st.session_state.candidate_info.items():
        if value:
            current_step += 1
    
    # Add progress for technical questions
    if st.session_state.conversation_state == "asking_tech_questions":
        question_percentage = (st.session_state.questions_answered / max(len(st.session_state.tech_questions), 1))
        current_step += question_percentage
    elif st.session_state.conversation_state == "conversation_end":
        current_step = total_steps
    
    # Calculate percentage
    return min(int((current_step / total_steps) * 100), 100)

def display_candidate_info():
    """Display collected candidate information in a sidebar."""
    
    # Only show info when some fields are filled
    has_info = any(value for value in st.session_state.candidate_info.values())
    
    if has_info:
        with st.sidebar:
            st.header("Candidate Information")
            
            info = st.session_state.candidate_info
            
            if info["full_name"]:
                st.markdown(f"**Name:** {info['full_name']}")
            if info["email"]:
                st.markdown(f"**Email:** {info['email']}")
            if info["phone"]:
                st.markdown(f"**Phone:** {info['phone']}")
            if info["experience"]:
                st.markdown(f"**Experience:** {info['experience']}")
            if info["desired_position"]:
                st.markdown(f"**Desired Position:** {info['desired_position']}")
            if info["location"]:
                st.markdown(f"**Location:** {info['location']}")
            if info["tech_stack"]:
                st.markdown(f"**Tech Stack:** {info['tech_stack']}")
            
            # Add a restart button
            if st.button("Restart Interview", type="primary"):
                from utils.session_state import clear_session
                clear_session()
                st.rerun()