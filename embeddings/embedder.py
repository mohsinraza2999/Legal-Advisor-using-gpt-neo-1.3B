"""
Module: embedder.py
Loads HuggingFace embeddings.
"""

from langchain.embeddings import HuggingFaceEmbeddings

def get_embeddings(model_name: str):
    """
    Loads sentence embeddings using HuggingFace.
    
    Args:
        model_name (str): Name of the sentence transformer model.
    
    Returns:
        HuggingFaceEmbeddings: Embedding model object.
    """
    return HuggingFaceEmbeddings(model_name=model_name)