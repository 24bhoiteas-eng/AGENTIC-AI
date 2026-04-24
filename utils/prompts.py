# utils/prompts.py

def researcher_prompt(brand: str, raw_data: str) -> str:
    return f"""You are a Brand Perception Researcher.
Your job is to analyze raw search data about the brand "{brand}" and extract key findings.

RAW SEARCH DATA:
{raw_data}

Extract and organize the following:
1. BRAND OVERVIEW: What the brand is known for
2. PUBLIC PERCEPTION: How customers view the brand (with examples)
3. RECENT NEWS: Any recent notable events or controversies
4. SOCIAL SENTIMENT: What people are saying on social platforms
5. KEY THEMES: Top 3-5 recurring themes in the data

Be factual. Use evidence from the data. Do not hallucinate.
Format your response with clear section headers."""


def sentiment_prompt(brand: str, research_notes: str) -> str:
    return f"""You are a Brand Sentiment Analyst.
Analyze the following research notes about "{brand}" and provide a detailed sentiment analysis.

RESEARCH NOTES:
{research_notes}

Provide:
1. OVERALL SENTIMENT SCORE: Positive / Neutral / Negative (with % estimate)
2. POSITIVE THEMES: What people love (list with examples)
3. NEGATIVE THEMES: What people criticize (list with examples)
4. EMOTIONAL TONE: How customers emotionally feel about the brand
5. TRUST LEVEL: High / Medium / Low with reasoning

Be analytical and specific. Use data from the notes."""


def writer_prompt(brand: str, research: str, sentiment: str) -> str:
    return f"""You are a Senior Brand Strategist writing a formal Brand Audit Report.

BRAND: {brand}
RESEARCH FINDINGS: {research}
SENTIMENT ANALYSIS: {sentiment}

Write a complete Brand Audit Report with these sections:

# Brand Audit Report: {brand}

## 1. Executive Summary
(2-3 sentence overview)

## 2. Brand Reputation Analysis
(Detailed analysis of how the brand is perceived)

## 3. Messaging Consistency
(Is the brand's message consistent across channels?)

## 4. Positioning Gaps
(Where does the brand fall short vs. its positioning?)

## 5. Competitive Context
(Brief note on competitive standing based on data)

## 6. Key Recommendations
(3-5 actionable recommendations)

Use professional language. Be specific. Cite themes from the research."""


def judge_prompt(brand: str, report: str) -> str:
    return f"""You are an expert Brand Consultant evaluating an AI-generated Brand Audit Report.

BRAND: {brand}
REPORT TO EVALUATE:
{report}

Score this report on the following criteria (each out of 10):

1. ACCURACY (10): Are claims backed by evidence?
2. DEPTH (10): Is the analysis thorough?
3. CLARITY (10): Is it well-written and easy to understand?
4. ACTIONABILITY (10): Are recommendations practical?
5. STRUCTURE (10): Is the report well-organized?

Provide:
- Individual scores for each criterion
- TOTAL SCORE: X/50
- STRENGTHS: What the report does well
- IMPROVEMENTS: What could be better
- FINAL VERDICT: Excellent / Good / Acceptable / Needs Revision"""