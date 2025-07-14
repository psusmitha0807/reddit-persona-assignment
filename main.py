from utils.reddit_scraper import get_user_data
from utils.persona_builder import build_persona
import os
import sys

def extract_username(url):
    return url.strip("/").split("/")[-1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <Reddit User URL>")
        sys.exit(1)

    url = sys.argv[1]
    username = extract_username(url)

    posts, comments = get_user_data(username)

    if not posts and not comments:
        print("❌ Failed to retrieve Reddit content.")
        sys.exit(1)

    print(f"✅ Generating persona using Gemini for user: {username}...")

    persona = build_persona(posts, comments)

    print("\n📄 Persona Preview:\n")
    print(persona)

    os.makedirs("personas", exist_ok=True)
    output_path = f"personas/{username}_persona.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"\n✅ Persona saved: {output_path}")

    
