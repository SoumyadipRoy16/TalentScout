import streamlit as st

def apply_custom_styling():
    """Apply custom CSS to improve the UI aesthetics."""
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
        /* Main container styling */
        .main {
            background-color: #f8f9fa;
        }
        
        /* Chat container styling */
        .stChatMessage {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 0.5rem;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            animation: fadeIn 0.3s ease-in-out;
        }
        
        /* User message styling */
        .stChatMessage.user {
            background-color: #e6f2ff;
        }
        
        /* Assistant message styling */
        .stChatMessage.assistant {
            background-color: #f0f0f0;
        }
        
        /* Header styling */
        h1 {
            color: #2c3e50;
            font-size: 2.5rem !important;
            margin-bottom: 1rem !important;
            font-weight: 600 !important;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f1f3f8;
        }
        
        /* Progress bar styling */
        .stProgress > div > div {
            background-color: #1e88e5;
        }
        
        /* Button styling */
        .stButton > button {
            border-radius: 20px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            transition: all 0.3s;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Animation for typing effect */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Chat input styling */
        .stChatInputContainer {
            padding-top: 1rem;
            border-top: 1px solid #eaecef;
        }
        
        /* Custom footer */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f8f9fa;
            padding: 0.5rem;
            text-align: center;
            font-size: 0.8rem;
            color: #6c757d;
            border-top: 1px solid #eaecef;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Add custom footer
    st.markdown("""
    <div class="footer">
        TalentScout Hiring Assistant © 2025 | Powered by AI
    </div>
    """, unsafe_allow_html=True)