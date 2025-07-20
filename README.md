# Legal-Advisor-using-gpt-neo-1.3B
This project aims to build an AI-powered Legal Advisor that leverages natural language processing and vector search technology to provide users with legal guidance based on authoritative legal texts.
🔍 How It Works
User Input: The user submits a legal question via a prompt.

Vector Search: The question is embedded and used to query a vector database containing embeddings of a legal book.

Contextual Retrieval: Relevant sections from the book are retrieved based on semantic similarity.

AI Response: The user query and retrieved legal content are passed to GPT-Neo 1.3B, which generates a legal advisory response.

⚙️ Tech Stack
Text Embeddings: To represent legal content semantically.

Vector Database: (e.g. FAISS, Pinecone) for fast and relevant document retrieval.

GPT-Neo 1.3B: Open-source language model for generating legal advice.

Python: Core language for backend logic.

💼 Use Cases
Legal research assistance

Law student support

General legal literacy tool

⚠️ Disclaimer: This tool provides AI-generated responses and is not a substitute for professional legal advice.
