from core.analyzer import analyze_failure
from core.suggestor import get_suggestion
from llm_client import LLMClient
import argparse
import sys
from utils.history import get_last_commands


def main():
    parser = argparse.ArgumentParser(description="Suggest fixes for failed shell commands using a local LLM.")
    parser.add_argument('--hard', action='store_true', help='Use a sequence of commands from history for analysis')
    parser.add_argument('--command', type=str, help='The failed command to analyze')
    args = parser.parse_args()
    
    if args.hard:
        commands = get_last_commands()
        if not commands:
            sys.exit(1)

    if args.command:
        commands = [args.command]
    else:
        return

    command_context = '\n'.join(commands)
    context = analyze_failure(command_context)

    llm = LLMClient()
    suggestion = get_suggestion(llm, context)

    print(suggestion)
    return

if __name__ == "__main__":
    main()