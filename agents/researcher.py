# agents/researcher.py

from utils.search import search_brand
from utils.prompts import researcher_prompt
from utils.llm import get_response          # ← replaces genai import

def run_researcher(brand: str) -> dict:
    print(f"[Researcher] Searching for brand: {brand}")

    reviews_data = search_brand(f"{brand} customer reviews 2024")
    news_data = search_brand(f"{brand} brand news reputation 2024")
    social_data = search_brand(f"{brand} social media public opinion")

    raw_data = f"""=== CUSTOMER REVIEWS ===\n{reviews_data}
=== NEWS & MEDIA ===\n{news_data}
=== SOCIAL MENTIONS ===\n{social_data}"""

    prompt = researcher_prompt(brand, raw_data)
    research_notes = get_response(prompt)           # ← replaces model.generate_content

    print(f"[Researcher] ✓ Research complete")

    return {
        "brand": brand,
        "raw_data": raw_data,
        "research_notes": research_notes
    }