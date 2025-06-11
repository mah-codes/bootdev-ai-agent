import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    verbose = '--verbose' in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not args:
        print("no prompt provided, exiting program..")
        print("Expected usage: python3 main.py 'YOUR PROMPT HERE'")
        sys.exit(1) 
    cli_prompt = " ".join(args)

    messages = [
            types.Content(role="user", parts=[types.Part(text=cli_prompt)]) 
    ]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    if verbose:
        print("User prompt:", cli_prompt)
    print(response.text)
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()