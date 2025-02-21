import cohere
from config import COHERE_API_KEY
from prompts import get_general_prompt, get_project_current_prompt, get_fomo_prompt

co = cohere.Client(COHERE_API_KEY)

def get_prompt_by_topic(topic):
    """Retrieve the appropriate prompt based on detected topic."""
    if topic == "project_current":
        return get_project_current_prompt()
    elif topic == "fomo":
        return get_fomo_prompt()
    
    return get_general_prompt()  # Default prompt

def generate_response(user_message, topic, emotion):
    """Generate a response using AI based on topic and detected emotion."""
    prompt = get_prompt_by_topic(topic)
    full_prompt = f"""
{prompt}

User message: {user_message}
Detected emotion: {emotion}
Assistant response:
"""

    response = co.generate(
        model='command-xlarge-nightly',
        prompt=full_prompt,
        max_tokens=100,
        temperature=0.5
    )

    return response.generations[0].text.strip()
