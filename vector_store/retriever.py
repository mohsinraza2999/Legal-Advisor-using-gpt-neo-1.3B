"""
Module: retriever.py
Creates and queries a FAISS vector store.
"""

from langchain.vectorstores import FAISS

def create_vectorstore(chunks, embedding_model):
    """
    Creates a FAISS vector store from document chunks and embeddings.
    
    Args:
        chunks (list): List of document chunks.
        embedding_model: HuggingFace embedding model.
    
    Returns:
        FAISS: FAISS vector store.
    """
    return FAISS.from_documents(chunks, embedding_model)

def search_vectorstore(vectorstore, query, k=2):
    """
    Searches the vector store for the top-k similar documents.
    
    Args:
        vectorstore (FAISS): The vector store.
        query (str): Search query.
        k (int): Number of top results to return.
    
    Returns:
        list: Retrieved documents.
    """
    return vectorstore.similarity_search(query, k=k)