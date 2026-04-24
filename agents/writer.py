# agents/writer.py

from utils.prompts import writer_prompt
from utils.llm import get_response

def run_article_writer(analogy_output: dict) -> dict:
    topic = analogy_output["topic"]
    research_notes = analogy_output["research_notes"]
    analogy_analysis = analogy_output["analogy_analysis"]

    print(f"[Writer] Writing explainer article for: {topic}")

    prompt = writer_prompt(topic, research_notes, analogy_analysis)
    article = get_response(prompt)

    print(f"[Writer] ✓ Article written")

    return {
        "topic": topic,
        "research_notes": research_notes,
        "analogy_analysis": analogy_analysis,
        "audit_report": article        # kept as audit_report so judge.py & app.py work unchanged
    }