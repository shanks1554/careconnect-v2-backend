import os
import requests
from dotenv import load_dotenv
from helpers.watsonx_auth import get_iam_token

load_dotenv()

PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
MODEL_ID = os.getenv("WATSONX_MODEL_ID")
BASE_URL = os.getenv("WATSONX_BASE_URL")

def generate_response_from_granite(prompt: str, max_tokens: int = 200) -> str:
    access_token = get_iam_token()

    url = f"{BASE_URL}/ml/v1/text/generation?version=2024-05-28"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    payload = {
        "model_id": MODEL_ID,
        "input": prompt,
        "project_id": PROJECT_ID,
        "parameters": {
            "decoding_method": "sample",
            "max_new_tokens": max_tokens,
            "temperature": 0.4,
            "top_p": 0.9
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Granite API Error {response.status_code}: {response.text}")

    return response.json()["results"][0]["generated_text"]