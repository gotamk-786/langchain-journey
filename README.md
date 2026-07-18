# LangChain Journey 🦜🔗

A hands-on learning repository documenting my journey through **LangChain** — covering LLMs, Chat Models, and Embedding Models across multiple providers (OpenAI, Anthropic, Groq, Google Gemini, and Hugging Face).

Each folder is a self-contained set of runnable examples, progressing from basic LLM calls to chat-based interactions and vector embeddings.

## 📁 Project Structure

```
Langchain/
├── 1.LLMs/                  # Basic LLM completion calls
│   ├── 1_llm_demo_groq.py       # Groq-hosted LLaMA 3.3 70B
│   └── 1_llm_demo_openAi.py     # OpenAI completion model
│
├── 2.ChatModels/            # Chat-based model interactions
│   ├── 1_chatmodel_openai.py    # OpenAI chat model
│   ├── 2_chatmodel_anthropic.py # Anthropic Claude chat model
│   ├── 3_chatmodel_hf_api.py    # Hugging Face Inference API (remote)
│   └── 4_huggingface_local.py   # Hugging Face model running locally
│
├── 3.EmbeddingModels/       # Text embedding generation
│   ├── 1_embedding_openai_query.py   # Single query embedding
│   └── 2_embedding_openai_docs.py    # Multi-document embedding
│
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/gotamk-786/langchain-journey.git
cd langchain-journey
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with your API keys:

```env
OPENAI_API_KEY="your-openai-key"
ANTHROPIC_API_KEY="your-anthropic-key"
GROQ_API_KEY="your-groq-key"
GOOGLE_API_KEY="your-google-key"
HUGGINGFACEHUB_API_TOKEN="your-huggingface-token"
```

> ⚠️ Never commit your `.env` file — it's already excluded via `.gitignore`.

### 5. Run any example

```bash
cd 2.ChatModels
python 3_chatmodel_hf_api.py
```

## 🧩 What This Covers

| Category | Concepts Explored |
|---|---|
| **LLMs** | Basic text-completion calls, comparing paid vs. free-tier providers |
| **Chat Models** | Multi-provider chat interfaces (OpenAI, Anthropic, Hugging Face — API & local) |
| **Embedding Models** | Query and document embeddings for semantic search / similarity |

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/)
- [Anthropic](https://www.anthropic.com/)
- [Groq](https://groq.com/)
- [Hugging Face](https://huggingface.co/)
- Python 3.10+

## 📌 Notes

- The Hugging Face examples use the new [Inference Providers](https://huggingface.co/docs/inference-providers) routing — not every model is available on every provider, so model choice matters.
- Local Hugging Face inference (`4_huggingface_local.py`) downloads and runs models on your machine via `transformers` — no API key required, but it needs sufficient disk space/RAM.

## 📄 License

This project is for educational purposes as part of my personal LangChain learning journey.

---

⭐ If you find this useful for learning LangChain, feel free to star the repo!
