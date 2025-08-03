<h1>🧠Legal-Advisor-using-gpt-neo-1.3B</h1>

<p>An intelligent legal assistant that leverages Natural Language Processing (NLP), vector search, and open-source language models to provide legal guidance based on authoritative legal texts.</p>

<hr/>

<h2>🔍 How It Works</h2>

<ol>
  <li><strong>💬 User Input:</strong> The user submits a legal question or prompt through a simple interface.</li>
  <li><strong>📚 Semantic Search:</strong> The prompt is embedded and used to query a vector database containing semantic representations (embeddings) of a legal book.</li>
  <li><strong>📖 Contextual Retrieval:</strong> Relevant sections of the legal text are retrieved based on semantic similarity to the user's query.</li>
  <li><strong>🧠 AI-Powered Response:</strong> The original query and retrieved context are passed to <code>GPT-Neo 1.3B</code>, which generates a response grounded in legal context.</li>
</ol>

<hr/>

<h2>⚙️ Tech Stack</h2>

<ul>
  <li><strong>🧾 Text Embeddings:</strong> Converts legal content into high-dimensional vectors for semantic search.</li>
  <li><strong>📊 Vector Database:</strong> Efficient document storage and retrieval using FAISS, Pinecone, or similar tools.</li>
  <li><strong>🧠 GPT-Neo 1.3B:</strong> Open-source transformer model to generate legal insights.</li>
  <li><strong>🐍 Python:</strong> Core language for backend logic and system orchestration.</li>
</ul>

<hr/>

<h2>💼 Use Cases</h2>

<ul>
  <li>🧑‍🎓 <strong>Law Student Support:</strong> Quickly understand legal concepts and references.</li>
  <li>🧾 <strong>Legal Research Assistant:</strong> Automate lookup of relevant sections from legal texts.</li>
  <li>🧠 <strong>General Legal Literacy:</strong> Make legal knowledge more accessible to non-lawyers.</li>
</ul>

<hr/>

<blockquote>
  ⚠️ <strong>Disclaimer:</strong> This tool provides AI-generated responses for educational and informational purposes only. It is <strong>not a substitute</strong> for professional legal advice.
</blockquote>


<hr>

   <h2 style="color: #34495e;">📁 Directory Structure</h2>
   <pre style="background: #f4f4f4; padding: 15px; border: 1px solid #ddd;">
rag-system/
├── chunking/          # Document loading and chunking
├── embeddings/        # Embedding logic
├── vector_store/      # FAISS-based vector retrieval
├── prompts/           # Prompt templating
├── llm_interface/     # Local LLM loading (HuggingFace)
├── scripts/           # Main execution scripts
├── dataset/
│   └── raw/           # Place your .pdf files here
├── requirements.txt
└── README.html
    </pre>

   <hr>

   <h2 style="color: #34495e;">🚀 Getting Started</h2>

   <h3>1. Install Dependencies</h3>
    <pre style="background: #eef; padding: 10px; border-left: 5px solid #2980b9;">pip install -r requirements.txt</pre>

   <h3>2. Place Documents</h3>
    <p>Put your <code>.pdf</code> files into:</p>
    <pre style="background: #f4f4f4; padding: 10px;">data/raw/</pre>

   <h3>3. Run the Pipeline</h3>
    <pre style="background: #eef; padding: 10px; border-left: 5px solid #27ae60;">python scripts/run_rag.py</pre>

   <hr>

   <h2 style="color: #34495e;">📌 Components</h2>
    <ul>
        <li><strong>Corpus Loader</strong>: Loads and chunks PDFs.</li>
        <li><strong>Embeddings</strong>: Uses HuggingFace models like <code>all-MiniLM-L6-V2</code>.</li>
        <li><strong>Vector Store</strong>: FAISS-powered similarity search.</li>
        <li><strong>Prompting</strong>: Dynamic prompt construction from retrieved docs.</li>
        <li><strong>LLM Inference</strong>: Runs a local model (e.g., <code>EleutherAI/gpt-neo-1.3B</code>) using Transformers pipeline.</li>
    </ul>

   <hr>

   <h2 style="color: #34495e;">🛠 Customize</h2>
    <p>You can replace:</p>
    <ul>
        <li>PDF loader with web or CSV input.</li>
        <li>FAISS with Chroma or other vector stores.</li>
        <li>LLM with OpenAI, Claude, LLaMA, etc.</li>
    </ul>

   <hr>

   <h2 style="color: #34495e;">📜 License</h2>
    <p>This project is open-source and available under the <strong>MIT License</strong>.</p>

   <hr>

   <h2 style="color: #34495e;">👨‍💻 Author</h2>
    <p>Made with Mohsin Raza.</p>
