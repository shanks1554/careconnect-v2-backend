from helpers.watsonx_granite import generate_response_from_granite

def positive_agent(user_input: str):
    prompt = f"""
    You are a kind and supportive mental health assistant.

    A user just said something positive: "{user_input}"

    Reply with a warm, encouraging message. Your tone should be friendly and human. 
    Limit your response to **one or two sentences** and **no more than 30 words**. 
    Avoid poetic or formal language.
    """
    
    response = generate_response_from_granite(prompt)
    
    return {
        "agent": "positive_agent",
        "response": response.strip()
    }