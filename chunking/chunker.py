"""
Module: chunker.py
Handles loading PDF documents and splitting them into text chunks.
"""

from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_corpus(path: str):
    """
    Loads PDF files from a directory using PyPDFLoader.
    
    Args:
        path (str): Path to directory containing PDF files.
    
    Returns:
        list: List of loaded documents.
    """
    loader = DirectoryLoader(path, glob='*.pdf', loader_cls=PyPDFLoader)
    return loader.load()

def create_chunks(docs, chunk_size=400, chunk_overlap=40):
    """
    Splits documents into smaller chunks using a recursive character splitter.
    
    Args:
        docs (list): List of documents.
        chunk_size (int): Maximum size of each chunk.
        chunk_overlap (int): Overlap between chunks.
    
    Returns:
        list: List of document chunks.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)