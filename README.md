# 🤖 LLM Document Q&A App

A lightweight and scalable web app that lets users upload a PDF document and ask natural language questions about its contents. Built using **FastAPI**, **LangChain**, and **Hugging Face Transformers**, this project demonstrates an end-to-end pipeline from file ingestion to LLM-based answer generation.



---

## 🧠 Key Features

- 📄 **PDF Upload**: Accepts PDF documents via a web endpoint
- 🔎 **Semantic Search**: Uses vector embeddings (ChromaDB + Sentence Transformers)
- 🧠 **LLM Answering**: Powered by Hugging Face's `distilgpt2` and LangChain's RetrievalQA
- 🌐 **API-first Design**: Built using FastAPI for easy front-end integration

---

## 🧱 Tech Stack

| Layer        | Tools                                   |
|--------------|------------------------------------------|
| Backend      | `FastAPI`, `LangChain`, `Python`         |
| LLM          | `distilgpt2`, `Hugging Face Transformers`|
| Embeddings   | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store | `ChromaDB`                               |
| Frontend     | (Optional) `Streamlit` or `Gradio`       |
| Deployment   | Replit / Docker / Hugging Face Spaces    |



