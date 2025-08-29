from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets contents of a file at a given file_path as a single string. Contents are truncated at 10,000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to get file's contents from, relative to the working directory. Must be a file and not a directory.",
            ),
        },
    ),
)
