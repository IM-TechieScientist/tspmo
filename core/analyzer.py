# core/analyzer.py

def analyze_failure(command, error="", hard=False):
    """
    Prepare context for the LLM based on the failed command(s) and error message.
    If hard=True, prompt LLM to consider a sequence of commands.
    """
    if hard:
        prompt = (
            f"The following sequence of shell commands led to an error.\n"
            f"Commands:\n{command}\n"
            f"Analyze the sequence and suggest the correct command to fix the issue. Respond with just the command. If no command is found, respond with 'null' "
        )
    else:
        prompt = (
            f"""Give the correct linux command for this. {command}
            Respond with just the command in plain text. 
            Nothing else. """
        )
    return prompt
