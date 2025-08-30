from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_files_info import get_files_info

from google.genai import types

function_map = {
    'get_files_info': get_files_info,
    'get_file_content': get_file_content,
    'run_python_file': run_python_file,
    'write_file': write_file
}

def call_function(function_call_part, verbose=False):
    fn_name = function_call_part.name
    call_id = getattr(function_call_part, 'id', None)
    if verbose:
        print(f"Calling function: {fn_name}({function_call_part.args})") 
    else:
        print(f" - Calling function: {fn_name}")

    # hard-coded working directory of "./calculator" for safety in this project
    fn_args = {'working_directory': './calculator', **function_call_part.args}
    if fn_name in list(function_map.keys()):
        fn_result = function_map[fn_name](**fn_args)
        payload = {"result": fn_result}
    else:
        payload = {"error": f"Unknown function: {fn_name}"}
    return types.Content(
        role="user",
        parts=[
            types.Part.from_function_response(
                name=fn_name,
                # id=call_id,
                response=payload,
            )
        ],
    )
   