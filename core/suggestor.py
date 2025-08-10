# core/suggestor.py
from llm_client import LLMClient

def get_suggestion(llm: LLMClient, context: str) -> str:
    """
    Use the LLM to get a suggested fix for the failed command.
    """
    return llm.get_fix(context)