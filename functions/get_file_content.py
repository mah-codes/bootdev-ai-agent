import os
from config import READ_MAX_CHAR
import sys

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_tgt = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_tgt.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_tgt):
        return f'Error: {file_path} does not exist!'

    if not os.path.isfile(abs_tgt):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_tgt, 'r') as f:
            tgt_data = f.read(READ_MAX_CHAR)
            # flag will be 1 if longer than read limit
            flag = len(f.read(1))
    except Exception as e:
        return f'Error: {str(e)}'
    if flag:
        return f'{tgt_data}...File "{file_path}" truncated at 10000 characters'
    else:
        return tgt_data

    sys.exit(1)
