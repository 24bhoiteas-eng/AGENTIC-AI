
# 🔍 Brand Audit AI: Multi-Agent Report Generator

An **Agentic AI System** developed for a Semester IV Engineering project. This system automates the process of brand auditing by using multiple specialized AI agents to research, analyze, and evaluate a brand's online presence in real-time.

## 🚀 Overview
The system takes a brand name as input and orchestrates a pipeline of four distinct agents:
1.  **Perception Researcher:** Gathers live data (reviews, news, social mentions) via Tavily Search.
2.  **Sentiment Analyst:** Processes raw data to determine emotional tone and trust levels.
3.  **Report Writer:** Synthesizes all findings into a professional Markdown-formatted audit report.
4.  **LLM-as-Judge:** Evaluates the final report for accuracy, depth, and actionability.

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Search Engine:** [Tavily AI](https://tavily.com/) (LLM-optimized search)
* **LLM (Local):** [Ollama](https://ollama.com/) (Running `gemma3:1b`)
* **LLM (Cloud):** [Google Gemini 2.0 Flash](https://aistudio.google.com/) (Fallback/Production)

---

## 📂 Project Structure
```text
brand-audit-agent/
├── app.py              # Streamlit Web Interface
├── pipeline.py         # Multi-agent orchestrator logic
├── .env                # API Keys (Tavily & Gemini)
├── requirements.txt    # Python dependencies
├── agents/             # Agent logic modules
│   ├── researcher.py
│   ├── sentiment.py
│   ├── writer.py
│   └── judge.py
└── utils/              # Helper utilities
    ├── search.py       # Tavily Search integration
    ├── prompts.py      # LLM Prompt templates
    └── llm.py          # Unified LLM provider logic (Ollama/Gemini)
```

---

## 📥 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/brand-audit-agent.git
cd brand-audit-agent
```

### 2. Setup Virtual Environment (Windows)
```powershell
python -m venv venv
.\venv\Scripts\activate.bat
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Setup API Keys
Create a `.env` file in the root directory and add your keys:
```env
TAVILY_API_KEY=tvly-your-key-here
GEMINI_API_KEY=your-gemini-key-here
```

### 5. Setup Local LLM (Ollama)
1.  Download and install [Ollama](https://ollama.com/).
2.  Pull the required model:
    ```powershell
    ollama pull gemma3:1b
    ```

---

## 🚀 Running the App

### Test the Pipeline (CLI)
```powershell
python pipeline.py
```

### Run the Web UI
```powershell
streamlit run app.py
```

---

## 📦 Dependencies (`requirements.txt`)
The project requires the following libraries:
* `streamlit`: For the web dashboard.
* `tavily-python`: For AI-powered web searching.
* `google-generativeai`: For Gemini API integration.
* `ollama`: For local LLM inference.
* `python-dotenv`: For managing environment variables.

---


<img width="1498" height="425" alt="image" src="https://github.com/user-attachments/assets/c121d81f-f58d-4d49-989f-163ab027dbed" />
<img width="1411" height="958" alt="image" src="https://github.com/user-attachments/assets/e7cc4ce7-f84e-447e-b83f-75df73fe9668" />
<img width="1404" height="829" alt="image" src="https://github.com/user-attachments/assets/e5bfcb8a-9d61-4f03-abed-f7e51697910a" />
