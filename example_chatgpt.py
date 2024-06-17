import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

# Ensure you have the OpenAI API key set as an environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

message = "Hello!"

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    pprint(response.json())
else:
    pprint(f"Request failed with status code {response.status_code}: {response.text}")