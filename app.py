import streamlit as st
from utils.session_state import initialize_session_state
from utils.llm_handler import process_user_message
from components.chat_interface import render_chat_interface
from components.styling import apply_custom_styling

def main():
    # Set page configuration
    st.set_page_config(
        page_title="TalentScout Hiring Assistant",
        page_icon="👨‍💼",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom styling to improve UI
    apply_custom_styling()
    
    # Initialize session state for conversation management
    initialize_session_state()
    
    # Page header
    st.markdown("# 🤖 TalentScout Hiring Assistant")
    st.markdown("""
    Welcome to TalentScout's AI-powered Hiring Assistant. I'm here to help with the initial screening process 
    for technology positions. Let's get started!
    """)
    
    # Display chat interface
    render_chat_interface()
    
    # Handle user input
    if user_input := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Process user message and get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                message_placeholder = st.empty()
                # Process the message and display with typing effect
                process_user_message(user_input, message_placeholder)

if __name__ == "__main__":
    main()