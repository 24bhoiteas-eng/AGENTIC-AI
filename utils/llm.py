import os
from dotenv import load_dotenv
load_dotenv()

USE_OLLAMA = False
USE_GROQ = True  # ← switched to Groq

def get_api_key(key_name):
    try:
        import streamlit as st
        return st.secrets[key_name]
    except:
        return os.getenv(key_name)

def get_response(prompt: str) -> str:
    if USE_OLLAMA:
        return _ollama_response(prompt)
    elif USE_GROQ:
        return _groq_response(prompt)
    else:
        return _gemini_response(prompt)

def _groq_response(prompt: str) -> str:
    from groq import Groq

    api_key = get_api_key("GROQ_API_KEY")
    if not api_key:
        raise Exception("GROQ_API_KEY not found!")

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # fast & free
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return response.choices[0].message.content

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

    api_key = get_api_key("GEMINI_API_KEY")
    if not api_key:
        raise Exception("GEMINI_API_KEY not found!")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                wait = 30 * (attempt + 1)
                print(f"Rate limited. Waiting {wait}s... (attempt {attempt+1}/3)")
                time.sleep(wait)
            else:
                raise Exception(f"Gemini error: {str(e)}")

    raise Exception("Gemini failed after 3 retries — quota exceeded. Wait a few minutes.")
