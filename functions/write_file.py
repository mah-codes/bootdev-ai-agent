import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_tgt = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_tgt.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    # if file_path doesn't exist we write a NEW file
    # if not os.path.exists(abs_tgt):
    try:
        with open(abs_tgt, 'w') as file:
            length = file.write(content)
    except Exception as e:
        return f'Error: {str(e)}'
    # else, we overwrite the contents of said file
    
    return f'Successfully wrote to "{file_path}" ({length} characters written)'
