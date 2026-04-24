# agents/researcher.py

from utils.search import search_topic
from utils.prompts import researcher_prompt
from utils.llm import get_response

def run_researcher(topic: str) -> dict:
    print(f"[Researcher] Searching for topic: {topic}")

    concept_data = search_topic(f"{topic} explained simply beginner guide")
    mechanism_data = search_topic(f"{topic} how it works in depth")
    terminology_data = search_topic(f"{topic} key concepts terminology")

    raw_data = f"""=== BEGINNER EXPLANATIONS ===\n{concept_data}
=== HOW IT WORKS ===\n{mechanism_data}
=== KEY CONCEPTS & TERMS ===\n{terminology_data}"""

    prompt = researcher_prompt(topic, raw_data)
    research_notes = get_response(prompt)

    print(f"[Researcher] ✓ Research complete")

    return {
        "topic": topic,
        "raw_data": raw_data,
        "research_notes": research_notes
    }