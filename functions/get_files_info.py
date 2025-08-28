import os
from sys import argv
import sys

def get_files_info(working_directory, directory="."):
    """given a working_directory, prints 1 level down of files/dir details"""
    # print(f'working_directory: {working_directory}')
    # print(f'directory: {directory}')
    tgt_dir = os.path.join(working_directory, directory)
    abs_tgt = os.path.abspath(tgt_dir)
    abs_working = os.path.abspath(working_directory)

    if not abs_tgt.startswith(abs_working):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_tgt):
        return f'Error: "{directory}" is not a directory'

    # Actually getting the file info
    output = []
    for item in os.listdir(abs_tgt):
        abs_item = os.path.join(tgt_dir, item)
        size = os.path.getsize(abs_item)
        dir_bool = os.path.isdir(abs_item)
        output.append(f' - {item}: file_size={size} bytes, is_dir={dir_bool}')
    return '\n'.join(output)
