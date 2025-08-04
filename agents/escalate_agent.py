from helpers.watsonx_granite import generate_response_from_granite

def escalate_agent(user_input: str):
    prompt = f"""
    You are a mental health support assistant.

    A user just said something that may indicate distress or feeling overwhelmed:
    "{user_input}"

    Respond with calm and compassion. Acknowledge their feelings and gently suggest talking to someone they trust or a mental health professional. Do NOT give clinical advice.

    Keep your tone supportive, and keep the message under 50 words.
    """
    response = generate_response_from_granite(prompt)
    
    return {
        "agent":"escalate_agent",
        "response": response
    }