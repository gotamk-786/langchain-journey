# LangChain Journey 🦜🔗

A hands-on learning repository documenting my journey through **LangChain** — covering LLMs, Chat Models, Embedding Models, Prompt Engineering, Vector Stores, and a full Retrieval-Augmented Generation (RAG) pipeline, across multiple providers (OpenAI, Anthropic, Groq, Mistral, Google Gemini, and Hugging Face).

Each folder is a self-contained set of runnable examples, progressing from basic LLM calls all the way to a working RAG application with document retrieval.

## 📁 Project Structure

```
Langchain/
├── 1.LLMs/                        # Basic LLM completion calls
│   ├── 1_llm_demo_groq.py             # Groq-hosted LLaMA 3.3 70B
│   ├── 1_llm_demo_openAi.py           # OpenAI completion model (gpt-3.5-turbo-instruct)
│   ├── grog_chat.py                   # Another Groq completion demo
│   └── hugging_face.py                # HF Endpoint + ChatHuggingFace (TinyLlama)
│
├── 2.ChatModels/                  # Chat-based model interactions
│   ├── 1_chatmodel_openai.py          # OpenAI chat model
│   ├── 2_chatmodel_anthropic.py       # Anthropic Claude chat model
│   ├── 2_UI_updated_chatbot.py        # Streamlit chatbot with mood/persona selector (Mistral)
│   ├── 3_chatmodel_hf_api.py          # Hugging Face Inference API (remote, Qwen2.5-7B)
│   ├── 4_huggingface_local.py         # Hugging Face model running locally (TinyLlama)
│   ├── chatbot.py                     # CLI chatbot with mode selection (Mistral)
│   ├── mistral_chatmodel.py           # Minimal single-call ChatMistralAI demo
│   └── UI_Chatbot.py                  # Streamlit persona chatbot (Mistral)
│
├── 3.EmbeddingModels/              # Text embedding generation
│   ├── 1_embedding_openai_query.py    # Single query embedding (OpenAI)
│   ├── 2_embedding_openai_docs.py     # Multi-document embedding (OpenAI)
│   ├── 3_embedding_hf_local.py        # Local embeddings (HF MiniLM, free)
│   ├── 4_misrasl_embeding_docs.py     # Multi-document embedding (Mistral)
│   └── 5_misral_emb_text.py           # Single query embedding (Mistral)
│
├── prompt/                         # Prompt engineering & templates
│   ├── message_placeholder.py         # MessagesPlaceholder for chat history injection
│   ├── prompt_generator.py            # Builds & saves a reusable PromptTemplate (-> template.json)
│   ├── propmt_ui.py                   # Streamlit "Research Tool" (paper summarizer)
│   ├── reusable_use_template.py       # Research Tool loading the saved template
│   ├── chat_history.txt               # Sample chat history data
│   └── prompt_templates_code/         # Standalone lesson series (has its own README)
│       ├── 1_string_prompt.py             # String prompts
│       ├── 2_chat_prompt.py               # Chat prompts
│       ├── 3_few_shot_prompt.py           # Few-shot prompting
│       ├── 4_structured_output.py         # Structured output
│       ├── 5_output_parser.py             # Output parsers
│       ├── 6_movie_info_extractor.py      # Mini project: movie info extractor
│       └── 7_research_paper_explainer.py  # Mini project: Streamlit research explainer
│
├── CineSage proj/                  # Mini project: movie info extractor from free text
│   ├── 1_core.py                       # Structured Movie extraction (PydanticOutputParser)
│   ├── core.py                         # Free-text version (broader fields, prompt-only)
│   └── Uicore.py                       # Streamlit UI for the free-text extractor
│
├── RAG project/                    # Retrieval-Augmented Generation pipeline
│   ├── create_database.py             # Load PDF → split → embed (HF MiniLM) → store in Chroma
│   ├── main.py                        # Load Chroma DB → MMR retriever → ChatMistralAI Q&A loop
│   ├── bad_chunk.txt                  # Sample/debug text file
│   ├── chroma_db/                     # Persisted Chroma vector store (generated, not source)
│   ├── document loaders/              # Loader & text-splitter examples
│   │   ├── 1_text_loader.py               # TextLoader
│   │   ├── 1_char_text_spillter.py        # CharacterTextSplitter
│   │   ├── 2_pdf_loader.py                # PyPDFLoader
│   │   ├── 2_token_based_spillter.py      # TokenTextSplitter
│   │   ├── 3_recursive.py                 # RecursiveCharacterTextSplitter
│   │   ├── 3_web_base_loader.py           # WebBaseLoader (web scraping)
│   │   └── deeplearning.pdf, GRU.pdf, notes.txt   # Sample source documents
│   └── retrievers/
│       └── arixv.py                   # ArxivRetriever — fetch papers from arXiv
│
├── vector store/                   # Standalone vector store demo
│   └── DB.py                          # In-memory Chroma store from sample Documents (Mistral embeddings)
│
├── runnable/                        # LangChain Expression Language (LCEL) runnable primitives
│   ├── seq_Runable.py                  # RunnableSequence — chaining steps
│   ├── parallelRunable.py              # RunnableParallel — running branches concurrently
│   ├── runablePassthrough.py           # RunnablePassthrough — forwarding input untouched
│   └── Manualsequencerunnale.py        # Manually composed sequence (no LCEL sugar) for comparison
│
├── Tools/                           # Tool creation & tool-calling fundamentals
│   ├── custom_Tools.py                 # Defining simple custom @tool functions
│   ├── toolCalling.py                  # Manual tool-calling loop (bind → invoke → execute → respond)
│   ├── tollcall.py                     # Minimal single-tool call/response walkthrough
│   └── newsSummarizer.py               # Mini project: Tavily search + Mistral summarization chain
│
├── Agents/                          # Multi-tool agent with human-in-the-loop approval
│   ├── agents.py                       # Mini project: City Intelligence agent (weather + news tools, CLI)
│   └── app.py                          # Streamlit UI for the City Intelligence agent
│
├── chroma_db/ , chroma-db/          # Persisted vector stores from earlier experiments
├── template.json                   # Saved PromptTemplate (research-paper summarizer)
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
MISTRAL_API_KEY="your-mistral-key"
HUGGINGFACEHUB_API_TOKEN="your-huggingface-token"
TAVILY_API_KEY="your-tavily-key"           # required for Tools/newsSummarizer.py and Agents/
OPENWEATHER_API_KEY="your-openweather-key" # required for Agents/ (weather tool)
```

> ⚠️ Never commit your `.env` file — it's already excluded via `.gitignore`.

### 5. Run any example

```bash
cd 2.ChatModels
python 3_chatmodel_hf_api.py
```

### 6. Try the full RAG pipeline

```bash
cd "RAG project"
python create_database.py   # builds the Chroma vector store from a PDF
python main.py               # ask questions over the document (retrieval + Mistral)
```

### 7. Try the City Intelligence Agent

```bash
cd Agents
python agents.py          # CLI version (asks approval before each tool call)
streamlit run app.py      # Streamlit UI version
```

## 🧩 What This Covers

| Category | Concepts Explored |
|---|---|
| **LLMs** | Basic text-completion calls, comparing paid vs. free-tier providers |
| **Chat Models** | Multi-provider chat interfaces (OpenAI, Anthropic, Mistral, Hugging Face — API & local), Streamlit chatbots with persona/mood switching |
| **Embedding Models** | Query and document embeddings for semantic search / similarity (OpenAI, Mistral, Hugging Face) |
| **Prompt Engineering** | String/Chat/Few-shot prompts, structured output, output parsers, reusable saved templates, message history injection |
| **Mini Projects** | CineSage (movie info extractor), Research Paper Explainer/Summarizer Streamlit apps, News Summarizer (Tavily + Mistral), City Intelligence Agent (CLI + Streamlit) |
| **Vector Stores** | Building and querying a Chroma vector store from raw documents |
| **RAG Pipeline** | Document loading (PDF/text/web), chunking strategies (character/token/recursive splitters), embedding, persistence, retrieval (similarity/MMR), and Arxiv paper retrieval |
| **LCEL Runnables** | RunnableSequence, RunnableParallel, RunnablePassthrough, and manual (non-LCEL) chaining for comparison |
| **Tools & Tool-Calling** | Defining custom `@tool` functions, binding tools to a model, manual tool-call → execute → respond loop |
| **Agents** | Multi-tool agent (weather + news) with human-in-the-loop approval before executing a tool call, in both CLI and Streamlit form |

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/) (`langchain`, `langchain-community`, `langchain-huggingface`, `langchain-mistralai`, `langchain-text-splitters`)
- [OpenAI](https://platform.openai.com/)
- [Anthropic](https://www.anthropic.com/)
- [Groq](https://groq.com/)
- [Mistral AI](https://mistral.ai/)
- [Hugging Face](https://huggingface.co/) (`transformers`, `sentence-transformers`)
- [Chroma](https://www.trychroma.com/) — local vector database
- [Streamlit](https://streamlit.io/) — interactive UIs for chatbot/research-tool demos
- Python 3.10+

## 📌 Notes

- The Hugging Face examples use the new [Inference Providers](https://huggingface.co/docs/inference-providers) routing — not every model is available on every provider, so model choice matters.
- Local Hugging Face inference (`4_huggingface_local.py`) downloads and runs models on your machine via `transformers` — no API key required, but it needs sufficient disk space/RAM.
- The RAG pipeline's `create_database.py` sanitizes PDF text (`encode("utf-8", "ignore")`) before embedding, since some PDFs contain broken/lone Unicode surrogate characters (from math symbols) that crash the tokenizer otherwise.
- `retrievers/arixv.py` depends on the `arxiv` PyPI package; keep it pinned below v4 (`arxiv<4`), since `langchain-community`'s Arxiv utility still relies on the older `Search.results()` API that v4 removed.
- `prompt_templates_code/` has its own detailed README (in Roman-Urdu/English) walking through each numbered lesson file in order — check it out for a guided learning path through prompt templates.

## 📄 License

This project is for educational purposes as part of my personal LangChain learning journey.

---

⭐ If you find this useful for learning LangChain, feel free to star the repo!
