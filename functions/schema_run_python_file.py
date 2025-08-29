from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file at a given file_path, returning a output, a stderror, stdout and exit_code all as one string.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to run a .py file from, relative to the working directory. Must be a python file.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of arguments that python file being called may require. if none given, defaults to '[]'.",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="A string argument to pass to the python file.",
                ),
            ),
        },
    ),
)
