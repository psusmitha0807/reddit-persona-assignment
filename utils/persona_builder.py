import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def build_persona(posts, comments):
    prompt = (
        "You're an expert analyst. Based on the Reddit user's posts and comments below, build a detailed persona including:\n"
        "- Interests\n- Personality traits\n- Tone of voice\n"
        "- Profession or background (if guessable)\n- Political/religious views (if any)\n"
        "Also include 1–2 quotes from the Reddit activity to justify each point.\n\n"
        f"POSTS:\n{''.join(posts[:5])}\n\nCOMMENTS:\n{''.join(comments[:5])}"
    )

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    headers = {"Content-Type": "application/json"}

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            print("❌ Error parsing Gemini response:", e)
            return "Error: Could not parse Gemini response"
    else:
        print("❌ Gemini API error:", response.status_code, response.text)
        return "Error: Could not generate persona"





