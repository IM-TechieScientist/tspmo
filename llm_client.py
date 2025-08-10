# llm_client.py
# Handles communication with the local LLM (Qwen Coder via Ollama)
import requests
import os

class LLMClient:
    def __init__(self, base_url=None, model=None):
        self.base_url = base_url or os.environ.get('OLLAMA_BASE_URL', 'http://localhost:11434')
        self.model = model or os.environ.get('OLLAMA_MODEL', 'qwen2.5-coder:3b')

    def get_fix(self, context):
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": context,
            "stream": False
        }
        try:
            resp = requests.post(url, json=payload, timeout=5)
            resp.raise_for_status()
            return resp.json().get('response', '').strip()
        except Exception as e:
            return f"[LLM Error] {e}"
