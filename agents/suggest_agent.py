from helpers.watsonx_granite import generate_response_from_granite

def suggest_agent(user_input: str):
    prompt = f"""
    You are a supportive mental health assistant. Based on the user's input, provide one gentle and helpful suggestion or coping strategy.

    Strict rules:
    - Do NOT ask any questions. Avoid any phrasing that sounds like a question.
    - Avoid starting sentences with "How about", "Would you", "Could you", "Maybe", "Why not", or anything that implies a question.
    - Only write a direct, compassionate statement.
    - DO NOT offer choices or ask for user input.
    - Keep it short and concise: only 2–3 sentences, no more than 3 lines.
    - Keep the tone warm, encouraging, and supportive.

    User input: "{user_input}"

    Suggestion:
    """

    response = generate_response_from_granite(prompt)

    return {
        "agent": "suggest_agent",
        "response": response.strip()
    }