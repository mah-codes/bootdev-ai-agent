import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    print("Hello from bootdev-ai-agent!")
    
    flags = []
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        contents = args[0]
    else:
        sys.exit(1)
    if len(args) > 1:
        flags = args[1:]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=contents
    )

    print(response.text)
    if "--verbose" in flags:
        print(f'User prompt: {contents}')
        print(f'Prompt tokens:', response.usage_metadata.prompt_token_count)
        print(f'Response tokens:', response.usage_metadata.candidates_token_count)
    

if __name__ == "__main__":
    main()
