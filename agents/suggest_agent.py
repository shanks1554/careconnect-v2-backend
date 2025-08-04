from helpers.watsonx_granite import generate_response_from_granite

def suggest_agent(user_input: str):
    prompt = f"""
    You are a supportive mental health assistant. Based on the user's input, provide a gentle, positive suggestion or coping strategy in 1–2 sentences.

    - Do not repeat the user's input.
    - Do not ask any follow-up questions.
    - Do not use phrases like "Would you like to..." or "Do you want to...".
    - Just make a warm, encouraging, and helpful statement.
    - Keep your answer short: no more than 2–3 sentences.
    - Keep it under 3 lines.

    User input: "{user_input}"

    Suggestion:
    """

    response = generate_response_from_granite(prompt)

    return {
        "agent": "suggest_agent",
        "response": response.strip()
    }