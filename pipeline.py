# pipeline.py

import time
from agents.researcher import run_researcher
from agents.sentiment import run_sentiment_analyst
from agents.writer import run_report_writer
from agents.judge import run_judge

def run_brand_audit(brand_name: str) -> dict:
    print(f"\n{'='*50}")
    print(f"Starting Brand Audit for: {brand_name}")
    print(f"{'='*50}\n")

    # Stage 1: Research
    researcher_output = run_researcher(brand_name)
    print("⏳ Waiting 20s to respect rate limits...")
    time.sleep(20)                                    # ← Wait between calls

    # Stage 2: Sentiment
    sentiment_output = run_sentiment_analyst(researcher_output)
    print("⏳ Waiting 20s to respect rate limits...")
    time.sleep(20)

    # Stage 3: Write Report
    writer_output = run_report_writer(sentiment_output)
    print("⏳ Waiting 20s to respect rate limits...")
    time.sleep(20)

    # Stage 4: Judge
    final_output = run_judge(writer_output)

    print(f"\n{'='*50}")
    print(f"Brand Audit Complete!")
    print(f"{'='*50}\n")

    return final_output

if __name__ == "__main__":
    result = run_brand_audit("Nike")
    print("\n--- AUDIT REPORT ---\n")
    print(result["audit_report"])
    print("\n--- JUDGE EVALUATION ---\n")
    print(result["judge_evaluation"])