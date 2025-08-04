from helpers.watsonx_granite import generate_response_from_granite
import json
import re

def generate_sentiment_emotion_prompt(text: str) -> str:
    return f"""
You are a helpful AI assistant. Analyze the sentiment and emotion of the following user message. Return a JSON object with only two keys: `sentiment` and `emotion`.

Sentiment should be one of: "positive", "negative", or "neutral".
Emotion should be the dominant emotion in the text (e.g., "joy", "anger", "sadness", "fear", "surprise", "disgust", etc.).

Respond only with a JSON object. No explanation or extra text.

Text: "{text}"
"""

def clean_emotion_label(emotion: str) -> str:
    emotion = emotion.lower()
    if "," in emotion:
        emotion = emotion.split(",")[0].strip()
    if emotion in ["none", "neutral", "no emotion"]:
        return "neutral"
    return emotion

def sentiment_agent(user_input: str):
    prompt = generate_sentiment_emotion_prompt(user_input)
    raw_response = generate_response_from_granite(prompt)

    # Clean up any extra markdown or quotes
    cleaned_response = raw_response.strip().strip('`"')
    cleaned_response = re.sub(r"^```json|```$", "", cleaned_response, flags=re.IGNORECASE).strip()

    try:
        result = json.loads(cleaned_response)
        sentiment = result.get("sentiment", "unknown").lower()
        emotion = clean_emotion_label(result.get("emotion", "neutral"))
    except (json.JSONDecodeError, AttributeError):
        sentiment = "unknown"
        emotion = "neutral"

    return {
        "agent": "sentiment_agent_granite",
        "sentiment": sentiment,
        "emotion": emotion,
        "raw_response": raw_response
    }