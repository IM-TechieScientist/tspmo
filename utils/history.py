import os
from typing import List

def get_last_commands(n: int = 5, history_file: str = None) -> List[str]:
    """
    Returns the last n commands from the shell history file.
    Tries to auto-detect bash or zsh history if not provided.
    """
    if not history_file:
        # Try to auto-detect
        home = os.path.expanduser('~')
        for candidate in ['.bash_history', '.zsh_history']:
            path = os.path.join(home, candidate)
            if os.path.exists(path):
                history_file = path
                break
    if not history_file or not os.path.exists(history_file):
        return []
    with open(history_file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines[-n:] if n > 0 else []
