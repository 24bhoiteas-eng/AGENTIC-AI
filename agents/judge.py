# agents/judge.py

from utils.prompts import judge_prompt
from utils.llm import get_response

def run_judge(writer_output: dict) -> dict:
    brand = writer_output["brand"]
    audit_report = writer_output["audit_report"]

    print(f"[Judge] Evaluating report for: {brand}")

    prompt = judge_prompt(brand, audit_report)
    evaluation = get_response(prompt)

    print(f"[Judge] ✓ Evaluation complete")

    return {
        "brand": brand,
        "research_notes": writer_output["research_notes"],
        "sentiment_analysis": writer_output["sentiment_analysis"],
        "audit_report": audit_report,
        "judge_evaluation": evaluation
    }