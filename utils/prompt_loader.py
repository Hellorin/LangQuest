import os
from typing import Dict

def load_prompt(prompt_name: str, variables: Dict[str, str] = None) -> str:
    """
    Load a prompt from a text file and replace variables if provided.
    
    Args:
        prompt_name: Name of the prompt file (without .txt extension)
        variables: Dictionary of variables to replace in the prompt
        
    Returns:
        The prompt text with variables replaced
    """
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to src, then to prompts
    prompts_dir = os.path.join(os.path.dirname(current_dir), "prompts")
    
    prompt_path = os.path.join(prompts_dir, f"{prompt_name}.txt")
    
    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            prompt = file.read()
            
        if variables:
            for key, value in variables.items():
                prompt = prompt.replace(f"{{{key}}}", value)
                
        return prompt
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}") 