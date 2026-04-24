# agents/judge.py

from utils.prompts import judge_prompt
from utils.llm import get_response

def run_judge(writer_output: dict) -> dict:
    topic = writer_output["topic"]
    article = writer_output["audit_report"]

    print(f"[Judge] Evaluating article for: {topic}")

    prompt = judge_prompt(topic, article)
    evaluation = get_response(prompt)

    print(f"[Judge] ✓ Evaluation complete")

    return {
        "topic": topic,
        "research_notes": writer_output["research_notes"],
        "sentiment_analysis": writer_output["analogy_analysis"],  # key kept for app.py compatibility
        "audit_report": article,
        "judge_evaluation": evaluation
    }