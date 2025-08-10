# llm_client.py
import requests
import os
import subprocess
import time
import socket


class LLMClient:
    def __init__(self, base_url=None, model=None):
        self.base_url = base_url or os.environ.get('OLLAMA_BASE_URL', 'http://localhost:11434')
        self.model = model or os.environ.get('OLLAMA_MODEL', 'qwen2.5-coder:3b')

        # Ensure Ollama is running
        if not self._is_server_running():
            self._start_ollama()

    def _is_server_running(self):
        try:
            host, port = self.base_url.replace("http://", "").split(":")
            with socket.create_connection((host, int(port)), timeout=1):
                return True
        except Exception:
            return False

    def _start_ollama(self):
        print("[INFO] Ollama not running. Starting...")
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Give it a few seconds to boot
        for _ in range(10):
            if self._is_server_running():
                print("[INFO] Ollama started successfully.")
                return
            time.sleep(0.5)
        raise RuntimeError("Failed to start Ollama within timeout.")

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
