import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

response = requests.get(url)

if response.status_code == 200:
    print("✅ Available models:")
    models = response.json().get("models", [])
    for model in models:
        print("-", model["name"])
else:
    print("❌ Failed to fetch models:", response.status_code, response.text)
