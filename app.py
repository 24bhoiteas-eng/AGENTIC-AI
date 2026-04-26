# app.py

import streamlit as st

# ── Page configuration ────────────────────────────────────────
st.set_page_config(
    page_title="Explainer Article Writer AI",
    page_icon="📝",
    layout="wide"
)

# ── Header ────────────────────────────────────────────────────
st.title("📝 Explainer Article Writer")
st.markdown("*Powered by a Multi-Agent AI System with LLM-as-Judge*")
st.divider()

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.header("ℹ️ How it works")
    st.markdown("""
    1. **Enter** a complex topic
    2. **Tavily** searches authoritative sources
    3. **3 AI Agents** process it:
       - 🔬 Concept Researcher
       - 🎯 Analogy Finder
       - ✍️ Article Writer
    4. **LLM Judge** scores the article on accuracy, simplicity & analogies
    """)
    st.divider()
    st.caption("Built with Python, Gemini/Ollama, Tavily & Streamlit")

# ── Main input ────────────────────────────────────────────────
col1, col2 = st.columns([3, 1])

with col1:
    topic_name = st.text_input(
        "Enter a complex topic",
        placeholder="e.g. Blockchain, CRISPR, Derivative Contracts, Quantum Computing...",
        label_visibility="collapsed"
    )

with col2:
    run_button = st.button("🚀 Generate Article", use_container_width=True, type="primary")

# ── Run the pipeline ──────────────────────────────────────────
if run_button:
    if not topic_name.strip():
        st.warning("Please enter a topic first.")
    else:
        progress_bar = st.progress(0, text="Starting article generation...")

        try:
            import time

            with st.spinner(""):
                progress_bar.progress(10, text="🔬 Researching core concepts with Tavily...")
                from agents.researcher import run_researcher
                researcher_output = run_researcher(topic_name)
                time.sleep(10)  # ← wait to avoid rate limit

                progress_bar.progress(40, text="🎯 Finding analogies and real-world examples...")
                from agents.analogy import run_analogy_finder
                analogy_output = run_analogy_finder(researcher_output)
                time.sleep(10)  # ← wait to avoid rate limit

                progress_bar.progress(65, text="✍️ Drafting beginner-friendly article...")
                from agents.writer import run_article_writer
                writer_output = run_article_writer(analogy_output)
                time.sleep(10)  # ← wait to avoid rate limit

                progress_bar.progress(85, text="⚖️ Judge evaluating accuracy & clarity...")
                from agents.judge import run_judge
                result = run_judge(writer_output)

                progress_bar.progress(100, text="✅ Complete!")

            time.sleep(0.5)
            progress_bar.empty()

            st.success(f"✅ Explainer Article for **{topic_name}** is ready!")
            st.divider()

            # ── Output in tabs ────────────────────────────────
            tab1, tab2, tab3, tab4 = st.tabs([
                "📄 Explainer Article",
                "🎯 Analogies & Examples",
                "🔬 Research Notes",
                "⚖️ Judge Evaluation"
            ])

            with tab1:
                st.markdown(result["audit_report"])
                st.download_button(
                    "📥 Download Article",
                    data=result["audit_report"],
                    file_name=f"{topic_name.replace(' ', '_')}_explainer.md",
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
