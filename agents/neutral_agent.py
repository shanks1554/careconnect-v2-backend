from helpers.watsonx_granite import generate_response_from_granite

def neutral_agent(user_input: str):
    prompt = f"""
    You are a warm and attentive mental health assistant.

    A user just said: "{user_input}"

    Respond with a short, gentle message that acknowledges their input and gently encourages them to share more. Keep the tone natural and warm. Avoid giving examples or generating a list. Keep it under 30 words.
    """
    response = generate_response_from_granite(prompt)
    
    return {
        "agent":"neutral_agent",
        "response": response
    }