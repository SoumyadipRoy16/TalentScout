# TalentScout Hiring Assistant

## Project Overview

TalentScout Hiring Assistant is an AI-powered chatbot designed to assist in the initial screening of candidates for technology positions. The chatbot collects essential candidate information and generates relevant technical questions based on the candidate's declared technology stack.

## Features

- **User-friendly Interface**: Clean and intuitive UI with a chat-based interaction model
- **Information Collection**: Gathers candidate details including name, email, phone, experience, desired position, location, and tech stack
- **Technical Assessment**: Generates tailored technical questions based on the candidate's tech stack
- **Context Awareness**: Maintains conversation context and provides a coherent flow
- **Responsive Design**: Works well on both desktop and mobile devices
- **Visual Feedback**: Provides typing indicators and progress tracking
- **Data Privacy**: Handles candidate information securely

## Technical Stack

- **Frontend**: Streamlit for the user interface
- **Backend**: Python
- **LLM Integration**: Groq API with Llama 3 70B model
- **Data Handling**: Session state management for conversation context

## Installation Instructions

1. Clone the repository:
   ```
   git clone https://github.com/SoumyadipRoy16/talent-scout.git
   cd talentscout-hiring-assistant
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. Run the application:
   ```
   streamlit run app.py
   ```

6. Open your browser and navigate to `http://localhost:8501` to use the application.

## Usage Guide

1. Start the conversation by providing your name when prompted.
2. Answer the chatbot's questions about your contact information, experience, and skills.
3. The chatbot will generate technical questions based on your tech stack.
4. Answer the technical questions to complete the initial screening process.
5. Your information will be collected and stored for the recruitment team to review.

## Project Structure

- `app.py`: Main Streamlit application
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation
- `utils/`: Utility functions
  - `constants.py`: Constants and configuration
  - `llm_handler.py`: Groq API integration
  - `prompt_templates.py`: LLM prompt templates
  - `session_state.py`: Session state management
- `components/`: UI components
  - `chat_interface.py`: Chat UI components
  - `styling.py`: Custom UI styling

## Prompt Design

The prompt design for this project focuses on three main areas:

1. **Information Extraction**: Specialized prompts to extract specific information from user responses, with validation rules for each field.

2. **Technical Question Generation**: Structured prompts that generate relevant technical questions based on the candidate's tech stack, ensuring a mix of basic and advanced questions.

3. **Context Handling**: System prompts that maintain the conversation context and provide a coherent flow, including fallback mechanisms for unexpected inputs.

The prompts are designed to be clear, concise, and guide the language model to produce desired outputs without revealing sensitive information.

## Challenges & Solutions

1. **Challenge**: Ensuring consistent extraction of information from varied user inputs.  
   **Solution**: Implemented specialized extraction prompts with validation rules for each field.

2. **Challenge**: Generating relevant technical questions for diverse tech stacks.  
   **Solution**: Created a structured prompt system that focuses on practical knowledge and problem-solving abilities.

3. **Challenge**: Maintaining a natural conversation flow.  
   **Solution**: Implemented a state-based conversation system with typing effects and appropriate timing.

4. **Challenge**: Handling unexpected inputs gracefully.  
   **Solution**: Added fallback mechanisms and validation checks to guide users back to the main flow.

5. **Challenge**: Creating an engaging user experience.  
   **Solution**: Added visual feedback like typing indicators, progress tracking, and custom styling.

## Future Enhancements

- Sentiment analysis to gauge candidate emotions during the conversation
- Multilingual support for international candidates
- Integration with ATS (Applicant Tracking System)
- Enhanced validation and verification of candidate information
- Expanded technical question database for more specialized assessments

## License

This project is for educational purposes only.

## Acknowledgments

- Streamlit for the excellent UI framework
- Groq for providing the LLM API