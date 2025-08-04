from helpers.watsonx_granite import generate_response_from_granite

def affirm_agent(user_input: str):
    prompt = f"""
    You are a warm and supportive mental health assistant.

    A user just said something affirming or agreeable: "{user_input}"

    Reply with a brief and natural confirmation. Keep it under 30 words. 
    Be conversational, friendly, and emotionally aware.
    Avoid sounding robotic or overly formal.
    """
    response = generate_response_from_granite(prompt)
    
    return {
        "agent": "affirm_agent",
        "response": response
    }