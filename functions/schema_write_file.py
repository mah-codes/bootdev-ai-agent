from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content given as a paramater to the file_path relative to a working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to which the content is written. Does not create a new directory or nested directories. Does not concatenate, only overwrites!",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents, as a string, that will be written to the new file.",
            ),
        },
    ),
)
