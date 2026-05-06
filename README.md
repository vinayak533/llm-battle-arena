# ⚔️ LLM Battle Arena

> An automated LLM evaluation framework — pit two AI models against each other and let a third one judge the winner.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-0.14-purple?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-API-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🧠 What is This?

**LLM Battle Arena** implements the **LLM-as-a-Judge** pattern — a technique where one language model evaluates the outputs of two competing models based on defined quality criteria.

This project includes:
- ✅ A **Python backend** that runs real LLM battles via the Groq API
- ✅ A **web demo UI** with animated responses, live scoreboards, and battle history

---

## 🎯 How It Works

```
User Prompt
    │
    ├──► Model A  ──► Response A ──┐
    │                              ├──► Judge LLM ──► Winner + Reason
    └──► Model B  ──► Response B ──┘
```

The **Judge LLM** evaluates responses based on four criteria (in priority order):

| Priority | Criteria |
|----------|----------|
| 1 | ✅ Correctness |
| 2 | 📋 Completeness |
| 3 | 💡 Clarity |
| 4 | 🔒 Safety & Best Practices |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A [Groq API](https://console.groq.com/) account (free tier available)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/llm-battle-arena.git
cd llm-battle-arena

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your Groq API key and model names
```

### Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
LLM_A=llama3-8b-8192
LLM_B=mixtral-8x7b-32768
JUDGE_LLM=llama3-70b-8192
```

### Run

```bash
python main.py
```

---

## 🌐 Web Demo

Open `index.html` directly in your browser — no server needed.

> **Note:** The web UI is a standalone demo with simulated responses. To connect it to real LLMs, a Flask/FastAPI backend would be needed (see [Future Improvements](#-future-improvements)).

---

## 📁 Project Structure

```
llm-battle-arena/
├── main.py           # Core battle logic (Python + Groq API)
├── index.html        # Animated web demo UI
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variable template
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| LLM Framework | [LlamaIndex](https://www.llamaindex.ai/) |
| LLM Provider | [Groq API](https://groq.com/) |
| Frontend | HTML, Tailwind CSS, Vanilla JS |
| Environment | python-dotenv |

---

## 🔮 Future Improvements

- [ ] Flask/FastAPI backend to power the web UI with real LLM calls
- [ ] Dynamic prompt input instead of hardcoded test questions
- [ ] Multi-provider support (OpenAI, Anthropic, Ollama)
- [ ] Database persistence for scores and battle history
- [ ] Advanced scoring with per-criteria breakdown
- [ ] REST API for programmatic access

---

## 💡 Use Cases

- **LLM Benchmarking** — Compare models on domain-specific tasks
- **Automated Evaluation** — Build CI/CD pipelines for LLM quality checks
- **Research** — Study and improve LLM evaluation methodologies
- **Education** — Demonstrate AI capabilities in a visual, interactive way

---

## 👨‍💻 Author

**Vinayak** — BCA Graduate | Data Science & AI Enthusiast



---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
