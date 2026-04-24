# 📝 Explainer Article Writer — Multi-Agent AI System

> Give it any complex topic. Get back a beginner-friendly explainer article — researched, written, and evaluated by AI agents.

---

## 🧠 What It Does

Paste in a complex topic like **Blockchain**, **CRISPR**, **Derivative Contracts**, or **Quantum Computing** — and a pipeline of 3 specialized AI agents will:

1. **Research** authoritative explanations from the web (via Tavily)
2. **Find analogies** and real-world examples to simplify the concept
3. **Write** a structured, beginner-friendly explainer article
4. **Judge** the article on accuracy, simplicity, and analogy quality

---

## 🏗️ Project Structure

```
explainer-article-writer/
│
├── app.py                  # Streamlit frontend
├── pipeline.py             # Orchestrates all agents end-to-end
│
├── agents/
│   ├── researcher.py       # 🔬 Concept Researcher — searches & extracts core ideas
│   ├── analogy.py          # 🎯 Analogy Finder — finds comparisons & real-world examples
│   ├── writer.py           # ✍️ Article Writer — drafts the explainer article
│   └── judge.py            # ⚖️ LLM Judge — scores the article
│
└── utils/
    ├── llm.py              # LLM interface (Ollama or Gemini)
    ├── prompts.py          # All agent prompts
    └── search.py           # Tavily web search wrapper
```

---

## ⚙️ Agent Pipeline

```
User Input (Topic)
      │
      ▼
🔬 Concept Researcher        ← Tavily searches: explanations, mechanisms, terminology
      │
      ▼
🎯 Analogy Finder            ← Tavily searches: analogies, real-world examples
      │
      ▼
✍️  Article Writer           ← Drafts beginner-friendly explainer article
      │
      ▼
⚖️  LLM Judge                ← Scores on Accuracy / Simplicity / Analogy / Structure
      │
      ▼
📄 Final Article + Evaluation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/explainer-article-writer.git
cd explainer-article-writer
```

### 2. Install dependencies

```bash
pip install streamlit tavily-python python-dotenv google-generativeai ollama
```

### 3. Set up your `.env` file

Create a `.env` file in the root directory:

```env
TAVILY_API_KEY=your_tavily_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here   # Only needed if USE_OLLAMA = False
```

> Get your Tavily API key at [tavily.com](https://tavily.com)  
> Get your Gemini API key at [aistudio.google.com](https://aistudio.google.com)

### 4. Choose your LLM backend

Open `utils/llm.py` and set your preference:

```python
USE_OLLAMA = True   # True = local Ollama,  False = Gemini API
```

**If using Ollama (local):**
```bash
ollama serve
ollama pull gemma3:1b
```

**If using Gemini API:**
Just make sure `GEMINI_API_KEY` is set in your `.env` file.

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the app in your browser (usually `http://localhost:8501`)
2. Type a complex topic in the input box
3. Click **🚀 Generate Article**
4. Wait for all 4 agents to complete (~2-3 minutes)
5. Browse results across 4 tabs:

| Tab | Content |
|-----|---------|
| 📄 Explainer Article | The full beginner-friendly article |
| 🎯 Analogies & Examples | Analogies and real-world comparisons |
| 🔬 Research Notes | Raw concept extraction from web data |
| ⚖️ Judge Evaluation | Scores and feedback on the article |

6. Download the article as a `.md` file

---

## ⚖️ Judge Scoring Criteria

The LLM Judge evaluates every article on 5 dimensions:

| Criterion | Out of | What it checks |
|-----------|--------|----------------|
| Accuracy | 10 | Are facts technically correct? |
| Simplicity | 10 | Can a beginner understand it? |
| Analogy Quality | 10 | Are analogies apt and correctly mapped? |
| Real-World Relevance | 10 | Are examples concrete and relatable? |
| Structure & Flow | 10 | Is the article well-organized? |
| **Total** | **50** | |

---

## 🔧 Configuration

| Setting | File | Default |
|---------|------|---------|
| Switch LLM (Ollama/Gemini) | `utils/llm.py` | `USE_OLLAMA = True` |
| Change Ollama model | `utils/llm.py` | `gemma3:1b` |
| Change Gemini model | `utils/llm.py` | `gemini-2.0-flash` |
| Number of search results | `utils/search.py` | `max_results=5` |
| Rate limit wait time | `pipeline.py` | `20 seconds` |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web UI |
| [Tavily](https://tavily.com) | Real-time web search |
| [Ollama](https://ollama.com) | Local LLM inference |
| [Gemini API](https://aistudio.google.com) | Cloud LLM (alternative) |
| [Python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variables |

---

## 📌 Example Topics to Try

- `Blockchain`
- `CRISPR Gene Editing`
- `Derivative Contracts`
- `Quantum Computing`
- `How the Stock Market Works`
- `Neural Networks`
- `Black Holes`
- `Inflation`

---

<img width="1908" height="771" alt="image" src="https://github.com/user-attachments/assets/9b23c52b-bff0-4108-a1c1-9318a1d212bd" />
