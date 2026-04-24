# pipeline.py

import time
from agents.researcher import run_researcher
from agents.analogy import run_analogy_finder
from agents.writer import run_article_writer
from agents.judge import run_judge

def run_explainer(topic: str) -> dict:
    print(f"\n{'='*50}")
    print(f"Starting Explainer Article for: {topic}")
    print(f"{'='*50}\n")

    # Stage 1: Research core concepts
    researcher_output = run_researcher(topic)
    print("⏳ Waiting 20s to respect rate limits...")
    time.sleep(20)

    # Stage 2: Find analogies
    analogy_output = run_analogy_finder(researcher_output)
    print("⏳ Waiting 20s to respect rate limits...")
    time.sleep(20)

    # Stage 3: Write article
    writer_output = run_article_writer(analogy_output)
    print("⏳ Waiting 20s to respect rate limits...")
    time.sleep(20)

    # Stage 4: Judge evaluation
    final_output = run_judge(writer_output)

    print(f"\n{'='*50}")
    print(f"Explainer Article Complete!")
    print(f"{'='*50}\n")

    return final_output

if __name__ == "__main__":
    result = run_explainer("Blockchain")
    print("\n--- EXPLAINER ARTICLE ---\n")
    print(result["audit_report"])
    print("\n--- JUDGE EVALUATION ---\n")
    print(result["judge_evaluation"])