from google.genai import types
from functions.schema_get_files_info import schema_get_files_info
from functions.schema_get_file_content import schema_get_file_content
from functions.schema_run_python_file import schema_run_python_file
from functions.schema_write_file import schema_write_file

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
Any python files that are not listed in Function Declarations require no arguments.
"""
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

