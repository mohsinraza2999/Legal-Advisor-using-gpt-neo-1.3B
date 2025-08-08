"""
Module: local_llm.py
Loads a local HuggingFace LLM and wraps it in a LangChain pipeline.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms import HuggingFacePipeline
import torch

def load_local_llm(model_name: str):
    """
    Loads a local HuggingFace LLM and returns a LangChain-compatible LLM.
    
    Args:
        model_name (str): Name of the HuggingFace model.
    
    Returns:
        HuggingFacePipeline: LangChain-compatible LLM.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer,
                    max_new_tokens=256, return_full_text=True)
    return HuggingFacePipeline(pipeline=pipe)