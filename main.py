import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from agent_setup import available_functions
from agent_setup import system_prompt
from call_function import call_function

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
    verbose = '--verbose' in flags

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=contents,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )

    print(response.text)
    if response.function_calls:
        for fn_call in response.function_calls:
            print(f"Calling function: {fn_call.name}({fn_call.args})")
            # Need to call the actual function HERE:
            fn_result = call_function(fn_call, verbose)
            if not fn_result.parts[0].function_response.response:
                raise Exception(f'Error: no response from function {fn_call.name}')
            elif fn_result.parts[0].function_response.response and verbose:
                print(f"-> {fn_result.parts[0].function_response.response}")

    if verbose:
        print(f'User prompt: {contents}')
        print(f'Prompt tokens:', response.usage_metadata.prompt_token_count)
        print(f'Response tokens:', response.usage_metadata.candidates_token_count)
    

if __name__ == "__main__":
    main()
