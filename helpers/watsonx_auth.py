import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_iam_token():
    api_key = os.getenv("WATSONX_API_KEY")
    url = "https://iam.cloud.ibm.com/identity/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code != 200:
        raise Exception(f"IAM Token Error {response.status_code}: {response.text}")

    return response.json()["access_token"]
