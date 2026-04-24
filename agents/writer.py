# agents/writer.py

from utils.prompts import writer_prompt
from utils.llm import get_response

def run_report_writer(sentiment_output: dict) -> dict:
    brand = sentiment_output["brand"]
    research_notes = sentiment_output["research_notes"]
    sentiment_analysis = sentiment_output["sentiment_analysis"]

    print(f"[Writer] Writing report for: {brand}")

    prompt = writer_prompt(brand, research_notes, sentiment_analysis)
    audit_report = get_response(prompt)

    print(f"[Writer] ✓ Report written")

    return {
        "brand": brand,
        "research_notes": research_notes,
        "sentiment_analysis": sentiment_analysis,
        "audit_report": audit_report
    }