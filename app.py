# app.py

import streamlit as st
from pipeline import run_brand_audit

# ── Page configuration ────────────────────────────────────────
st.set_page_config(
    page_title="Brand Audit AI",
    page_icon="🔍",
    layout="wide"
)

# ── Header ────────────────────────────────────────────────────
st.title("🔍 Brand Audit Report Generator")
st.markdown("*Powered by a Multi-Agent AI System with LLM-as-Judge*")
st.divider()

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.header("ℹ️ How it works")
    st.markdown("""
    1. **Enter** a brand name
    2. **Tavily** searches live data
    3. **3 AI Agents** analyze it:
       - 🔎 Perception Researcher
       - 📊 Sentiment Analyst  
       - ✍️ Report Writer
    4. **LLM Judge** scores the report
    """)
    st.divider()
    st.caption("Built with Python, Gemini, Tavily & Streamlit")

# ── Main input ────────────────────────────────────────────────
col1, col2 = st.columns([3, 1])

with col1:
    brand_name = st.text_input(
        "Enter a brand name",
        placeholder="e.g. Nike, Apple, Tesla, Zara...",
        label_visibility="collapsed"
    )

with col2:
    run_button = st.button("🚀 Generate Report", use_container_width=True, type="primary")

# ── Run the pipeline ──────────────────────────────────────────
if run_button:
    if not brand_name.strip():
        st.warning("Please enter a brand name first.")
    else:
        # Progress tracking
        progress_bar = st.progress(0, text="Starting brand audit...")

        try:
            with st.spinner(""):
                # Show live progress steps
                progress_bar.progress(10, text="🔎 Searching the web with Tavily...")
                import time

                # Import and run each agent with progress updates
                from agents.researcher import run_researcher
                researcher_output = run_researcher(brand_name)
                progress_bar.progress(35, text="📋 Analyzing brand perception...")

                from agents.sentiment import run_sentiment_analyst
                sentiment_output = run_sentiment_analyst(researcher_output)
                progress_bar.progress(60, text="📊 Running sentiment analysis...")

                from agents.writer import run_report_writer
                writer_output = run_report_writer(sentiment_output)
                progress_bar.progress(85, text="✍️ Writing audit report...")

                from agents.judge import run_judge
                result = run_judge(writer_output)
                progress_bar.progress(100, text="✅ Complete!")

            time.sleep(0.5)
            progress_bar.empty()

            st.success(f"✅ Brand Audit for **{brand_name}** is ready!")
            st.divider()

            # ── Output in tabs ────────────────────────────────────────
            tab1, tab2, tab3, tab4 = st.tabs([
                "📄 Audit Report",
                "📊 Sentiment Analysis",
                "🔎 Research Notes",
                "⚖️ Judge Evaluation"
            ])

            with tab1:
                st.markdown(result["audit_report"])
                st.download_button(
                    "📥 Download Report",
                    data=result["audit_report"],
                    file_name=f"{brand_name}_audit_report.md",
                    mime="text/markdown"
                )

            with tab2:
                st.markdown(result["sentiment_analysis"])

            with tab3:
                st.markdown(result["research_notes"])

            with tab4:
                st.markdown(result["judge_evaluation"])

        except Exception as e:
            progress_bar.empty()
            st.error(f"An error occurred: {str(e)}")
            st.info("Check your API keys in the .env file and try again.")