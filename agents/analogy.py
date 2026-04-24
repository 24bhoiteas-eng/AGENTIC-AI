# agents/analogy.py

from utils.search import search_topic
from utils.prompts import analogy_prompt
from utils.llm import get_response

def run_analogy_finder(researcher_output: dict) -> dict:
    topic = researcher_output["topic"]
    research_notes = researcher_output["research_notes"]

    print(f"[Analogy Finder] Finding analogies for: {topic}")

    analogy_search = search_topic(f"{topic} analogy simple comparison everyday life")
    examples_search = search_topic(f"{topic} real world examples applications")

    extra_data = f"""=== ANALOGIES FROM WEB ===\n{analogy_search}
=== REAL WORLD EXAMPLES ===\n{examples_search}"""

    enriched_notes = research_notes + "\n\n" + extra_data

    prompt = analogy_prompt(topic, enriched_notes)
    analogy_output = get_response(prompt)

    print(f"[Analogy Finder] ✓ Analogies found")

    return {
        "topic": topic,
        "raw_data": researcher_output["raw_data"],
        "research_notes": research_notes,
        "analogy_analysis": analogy_output
    }