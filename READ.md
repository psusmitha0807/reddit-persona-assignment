# Reddit Persona Assignment

This project was developed as part of a generative AI internship assignment.  
The objective was to analyze Reddit user behavior and generate psychological personas using scraped data and Gemini LLMs.

---

## 🚀 Objective

- Scrape posts and comments from a given Reddit user.
- Analyze language patterns, tone, and content to infer:
  - Interests
  - Personality traits
  - Tone of voice
  - Profession or background
  - Political/religious views (if any)
- Generate a written persona with textual justifications and quotes.

---

## 🧠 Tech Stack

- Python 3.10+
- [PRAW](https://praw.readthedocs.io/en/stable/) – Reddit API Wrapper
- Google Gemini API (via MakerSuite)
- dotenv – For managing API keys securely
- requests – For API communication

---

## 🗂️ Project Structure

reddit-persona-assignment/
├── main.py
├── test_scrape.py
├── .env
├── requirements.txt
├── README.md
├── check_models.py
├── utils/
│ ├── reddit_scraper.py
│ └── persona_builder.py
├── personas/
│ ├── kojied_persona.txt
│ └── Hungry-Move-6603_persona.txt

