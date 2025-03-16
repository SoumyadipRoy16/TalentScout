"""Prompt templates for LLM interactions."""

# System prompt to guide the model's behavior
SYSTEM_PROMPT = """
You are an AI assistant for TalentScout, a recruitment agency specializing in technology placements.
Your role is to assist in the initial screening of candidates by gathering essential information and 
asking relevant technical questions based on the candidate's declared tech stack.

Be professional, concise, and friendly in your responses. 
Focus on extracting accurate information for the recruitment process.
"""

def get_information_extraction_prompt(user_message: str, info_type: str) -> str:
    """Generate a prompt for extracting specific information from user message.
    
    Args:
        user_message: User message to extract information from
        info_type: Type of information to extract
        
    Returns:
        Prompt for the LLM
    """
    # Base prompt structure
    base_prompt = f"""
    Extract the {info_type} from the following message:
    
    USER MESSAGE: {user_message}
    
    Return ONLY the extracted {info_type} without any additional text, explanations, or formatting.
    If you cannot find a valid {info_type}, respond with "NOT_FOUND".
    """
    
    # Add specific instructions based on info type
    if info_type == "name":
        base_prompt += """
        Extract the full name of the person. If only a first name is provided, return just that.
        Example: For "My name is John Smith", return "John Smith".
        """
    
    elif info_type == "email":
        base_prompt += """
        Extract a valid email address in the format username@domain.com.
        Example: For "You can reach me at john.smith@example.com", return "john.smith@example.com".
        """
    
    elif info_type == "phone":
        base_prompt += """
        Extract a valid phone number. Accept various formats including international formats.
        Example: For "My number is +1-555-123-4567", return "+15551234567".
        """
    
    elif info_type == "experience":
        base_prompt += """
        Extract the years of experience as a number or range.
        Example: For "I have been working for 5 years", return "5 years".
        For "I have 3-5 years of experience", return "3-5 years".
        """
    
    elif info_type == "position":
        base_prompt += """
        Extract the desired position or role the candidate is interested in.
        Example: For "I'd like to apply for the Software Engineer position", return "Software Engineer".
        For multiple positions, list them all separated by commas.
        """
    
    elif info_type == "location":
        base_prompt += """
        Extract the current location of the candidate, preferably as city and country.
        Example: For "I'm currently based in New York, USA", return "New York, USA".
        """
    
    elif info_type == "tech_stack":
        base_prompt += """
        Extract the technology stack mentioned, including programming languages, frameworks, databases, and tools.
        Example: For "I work with Python, Django, PostgreSQL, and Docker", return "Python, Django, PostgreSQL, Docker".
        List all technologies mentioned, separated by commas.
        """
    
    return base_prompt

def get_technical_questions_prompt(tech_stack: str) -> str:
    """Generate a prompt for creating technical questions based on tech stack.
    
    Args:
        tech_stack: Candidate's technology stack
        
    Returns:
        Prompt for the LLM
    """
    return f"""
    Based on the following technology stack, generate 5 relevant technical questions to assess a candidate's proficiency.
    
    TECH STACK: {tech_stack}
    
    Guidelines for questions:
    1. Questions should assess practical knowledge and problem-solving abilities.
    2. Include a mix of basic and advanced concepts for each technology.
    3. Focus on real-world applications and common challenges.
    4. Avoid questions that can be answered with a simple yes/no.
    5. Make sure questions are specific to the technologies mentioned.
    
    Format each question as a numbered list:
    1. [Question text]
    2. [Question text]
    3. [Question text]
    4. [Question text]
    5. [Question text]
    
    Do not provide answers to the questions.
    """