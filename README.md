# MindVault

A local RAG (Retrieval-Augmented Generation) system that runs entirely on your machine using [Ollama](https://ollama.com). Ask questions against your own text files — no cloud, no API keys.

## How it works

1. **Load** — reads `data.txt` from the project directory
2. **Chunk** — splits the text into overlapping sentence windows
3. **Embed** — converts each chunk into a vector using an Ollama embedding model
4. **Retrieve** — on each question, finds the top-k most relevant chunks via cosine similarity
5. **Generate** — sends the retrieved context plus the question to an Ollama chat model and prints the answer

## Project structure

```
src/mindvault/
├── rag.py                  # Entry point — runs the Q&A loop
├── data.txt                # Your knowledge base
└── components/
    ├── __init__.py         # Package exports
    ├── embedding.py        # embed()       — text → vector via Ollama
    ├── llm.py              # ask_llm()     — prompt → answer via Ollama
    ├── chunker.py          # chunk_text()  — split text into overlapping chunks
    ├── loader.py           # load_file()   — read data.txt from disk
    └── retriever.py        # build_index(), retrieve() — vector search
```

## Setup

1. Install [Ollama](https://ollama.com) and pull your models:
   ```bash
   ollama pull nomic-embed-text
   ollama pull llama3
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Copy `.env.example` to `.env` and fill in your values:
   ```
   OLLAMA=http://localhost:11434
   EMBED_MODEL=nomic-embed-text
   CHAT_MODEL=llama3
   ```

4. Add your content to `src/mindvault/data.txt`.

## Usage

```bash
uv run src/mindvault/rag.py
```

Then type any question at the prompt. Type `Ctrl+C` to exit.

## Requirements

- Python 3.9+
- Ollama running locally
