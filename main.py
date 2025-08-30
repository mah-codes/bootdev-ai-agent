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
    messages = []
    messages.append(types.Content(role="user", parts=[types.Part.from_text(text=contents)]))
    while interaction_count < 20:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
        )
        if response.text:
            print(response.text)
        else:
            print("---- ALL DONE ----")
            break
        for candidate in response.candidates:
            messages.append(candidate.content)
        if response.function_calls:
            for fn_call in response.function_calls:
                print(f"Calling function: {fn_call.name}({fn_call.args})")
                fn_result = call_function(fn_call, verbose)
                fn_response = fn_result.parts[0].function_response.response
                if not fn_response:
                    raise Exception(f'Error: no response from function {fn_call.name}')
                elif fn_response:
                    messages.append(fn_result)
                    print(f"-> {fn_response}")
            interaction_count += 1
    
    if verbose:
        print(f'User prompt: {contents}')
        print(f'Prompt tokens:', response.usage_metadata.prompt_token_count)
        print(f'Response tokens:', response.usage_metadata.candidates_token_count)
    

if __name__ == "__main__":
    main()
