# tspmo
Python CLI tool for fixing command-line errors using a local LLM (Qwen Coder via Ollama).
This tool captures wrong shell commands, sends them to a local LLM and suggests a fix. 

This is inspired by the [thefuck](https://github.com/nvbn/thefuck) CLI tool.

## Structure
- `cli.py`: CLI entry point
- `core/`: Main logic (analyzer, suggestor)
- `llm_client.py`: LLM communication
- `utils/`: Helpers
- `tests/`: Tests

## Requirements
- Python 3.8+
- Ollama with Qwen-2.5-Coder model installed and running locally.

## Installation
- Install Ollama.

  `curl -fsSL https://ollama.com/install.sh | sh`
- Install qwen2.5-coder:3b. (You may use a better model if your system can handle it)
  
  `ollama run qwen2.5-coder:3b`
- Clone this repository.
- Add the following lines to your ~/.bashrc
```bash
HISTIGNORE='tspmo*'

function tspmo {
    local last_cmd
    last_cmd="$(fc -ln -1)"
    local fixed_cmd
    fixed_cmd="$(python3 /home/<YOUR_USERNAME>/tspmo/cli.py --command "$last_cmd" "$@")" || return
    if [ -z "$fixed_cmd" ]; then
        echo "No suggestion found."
        return
    fi
    echo "Suggested fix:"
    echo "$fixed_cmd"
    read -p "[enter/ctrl+c]" _ || { echo "Cancelled."; return; }
    history -s "$fixed_cmd"
    eval "$fixed_cmd"
}
```