"""Constants and configuration for the TalentScout Hiring Assistant."""

# Conversation states
STATES = {
    "collecting_name": "collecting_name",
    "collecting_email": "collecting_email",
    "collecting_phone": "collecting_phone",
    "collecting_experience": "collecting_experience",
    "collecting_position": "collecting_position",
    "collecting_location": "collecting_location",
    "collecting_tech_stack": "collecting_tech_stack",
    "asking_tech_questions": "asking_tech_questions",
    "conversation_end": "conversation_end",
}

# Maximum number of technical questions to ask
MAX_TECH_QUESTIONS = 5

# List of exit keywords that will end the conversation
EXIT_KEYWORDS = ["exit", "quit", "end", "stop", "bye", "goodbye"]

# Regular expressions for validation
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\+?[0-9]{10,15}$'

# Common technology stacks for suggestions
TECH_STACK_EXAMPLES = [
    "Python, Django, PostgreSQL, Docker",
    "JavaScript, React, Node.js, MongoDB",
    "Java, Spring Boot, MySQL, AWS",
    "C#, .NET, SQL Server, Azure",
    "Ruby, Rails, PostgreSQL, Heroku",
]

# Common tech positions
TECH_POSITIONS = [
    "Software Engineer",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Data Scientist",
    "DevOps Engineer",
    "Machine Learning Engineer",
    "Mobile Developer",
    "UI/UX Designer",
    "QA Engineer",
]

# Typing effect configuration
TYPING_SPEED = 0.01  # Seconds per character