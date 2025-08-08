"""
Module: builder.py
Creates prompts using retrieved context.
"""

from langchain.prompts import PromptTemplate

def build_prompt_template(query: str, retrieved_docs: list):
    """
    Builds a prompt template with context and query.
    
    Args:
        query (str): The user query.
        retrieved_docs (list): Retrieved context documents.
    
    Returns:
        PromptTemplate: Formatted LangChain prompt.
    """
    context = retrieved_docs[0].page_content
    page = retrieved_docs[1].metadata.get("page", "unknown")

    template = f"""
    Given the context below, answer the question.
    Question: {query}
    Context: {context}\n\n(Page {page})
    Remember to answer only based on the context provided and not from any other source.
    If the question cannot be answered based on the provided context, say "I don't know."
    """

    return PromptTemplate(input_variables=["retrieved_context", "query"], template=template)