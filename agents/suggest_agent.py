from helpers.watsonx_granite import generate_response_from_granite

def suggest_agent(user_input: str):
    prompt = f"""
    You are a compassionate mental health assistant. The user is going through something emotionally challenging. 
    Respond with a warm, encouraging, and emotionally supportive message. 
    Avoid giving any suggestions, advice, coping strategies, or exercises like breathing, grounding, or journaling. 
    Focus only on comfort and support.

    User input: "{user_input}"

    Supportive response:
    """
    response = generate_response_from_granite(prompt)

    return {
        "agent": "suggest_agent",
        "response": response.strip()
    }