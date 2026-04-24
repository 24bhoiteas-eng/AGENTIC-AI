# agents/sentiment.py

from utils.prompts import sentiment_prompt
from utils.llm import get_response

def run_sentiment_analyst(researcher_output: dict) -> dict:
    brand = researcher_output["brand"]
    research_notes = researcher_output["research_notes"]

    print(f"[Sentiment] Analyzing sentiment for: {brand}")

    prompt = sentiment_prompt(brand, research_notes)
    sentiment_analysis = get_response(prompt)

    print(f"[Sentiment] ✓ Sentiment analysis complete")

    return {
        "brand": brand,
        "raw_data": researcher_output["raw_data"],
        "research_notes": research_notes,
        "sentiment_analysis": sentiment_analysis
    }