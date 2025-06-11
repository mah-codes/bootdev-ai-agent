import os

def get_files_content(working_directory, file_path):
    try: 
        out_of_scope = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        pwd = os.path.abspath(working_directory)
        abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))
        if  pwd != abs_filepath[:len(pwd)]:
            return out_of_scope
        elif not os.path.isfile(abs_filepath):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f"Error: {e}"

    with open(abs_filepath, 'r') as f:
        file_content = f.read()
        if len(file_content) > 10000:
            file_content = file_content[:10000] + f'...File "{file_path}" truncated at 10000 characters'
    return file_content

    
    
    