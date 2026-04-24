# utils/llm.py

import os
from dotenv import load_dotenv

load_dotenv()

USE_OLLAMA = False  # True = Ollama (local), False = Gemini (API)


def get_response(prompt: str) -> str:
    if USE_OLLAMA:
        return _ollama_response(prompt)
    else:
        return _gemini_response(prompt)


def _ollama_response(prompt: str) -> str:
    import ollama
    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


def _gemini_response(prompt: str) -> str:
    import google.generativeai as genai
    import time

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")

    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                wait = 30 * (attempt + 1)
                print(f"Rate limited. Waiting {wait}s...")
                time.sleep(wait)
            else:
                raise e
    raise Exception("Gemini failed after 3 retries")
