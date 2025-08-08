"""
Script: run_rag.py
Main script to execute the full RAG pipeline.
"""

from chunking.chunker import load_corpus, create_chunks
from embeddings.embedder import get_embeddings
from vector_store.retriever import create_vectorstore, search_vectorstore #use to search from the vector database
from prompts.builder import build_prompt_template #use to build custom template
from llm_interface.local_llm import load_local_llm
from langchain.chains import RetrievalQA

# Step 1: Load and chunk corpus
corpus = load_corpus("dataset/raw/")
chunks = create_chunks(corpus, chunk_size=400, chunk_overlap=40)

# Step 2: Embed chunks
embedding_model = get_embeddings("sentence-transformers/all-MiniLM-L6-V2")
vectorstore = create_vectorstore(chunks, embedding_model)


# Step 3: Load LLM and run RetrievalQA
llm = load_local_llm("EleutherAI/gpt-neo-1.3B")





qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever(search_kwargs={"k": 2}), return_source_documents=True)


# Step 4: Query
#query = "What is the significance of the Official Journal of the European Union, specifically issue L 119?"
query:str= str(input("ask your legal quary"))
#retrieved_docs = search_vectorstore(vectorstore, query, k=2)

# Step 5: Build prompt

#prompt_template = build_prompt_template(query, retrieved_docs)

#result= llm(prompt_template)   #used for custom template


# Step 6: Get result
result = qa_chain({"query": query})
print(result["result"])