import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from test_agent_setup import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    
    flags = []
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        contents = args[0]
    else:
        sys.exit(1)
    if len(args) > 1:
        flags = args[1:]
    verbose = '--verbose' in flags
    
    interaction_count = 0
    messages = [{'role': 'initial query', 'content': contents}]
    while interaction_count < 5:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )
        print(response.text)
        messages.append({'role': 'assistant', 'content': response.text})
        user_input = input("Your answer: ")
        messages.append({'role': 'user', 'content': user_input})
        contents = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
        interaction_count += 1

    if verbose:
        print(f'Full conversation: {contents}')
        print(f'Prompt tokens:', response.usage_metadata.prompt_token_count)
        print(f'Response tokens:', response.usage_metadata.candidates_token_count)
    

if __name__ == "__main__":
    main()
