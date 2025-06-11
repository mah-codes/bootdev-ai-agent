import os
from itertools import accumulate

def write_file(working_directory, file_path, content):
    out_of_scope = f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    pwd = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, file_path))
    if  pwd != os.path.commonpath([pwd, abs_directory]):
        return out_of_scope
    # Now that we know we're in the correct directory and pwd == base:
    # Start with the working_directory, concatenating next-level directories
    # Check if this exsits: YES continue; NO create & continue
    file_path_list = dirs_to_cwd(file_path)
    paths_to_check = list(accumulate(file_path_list, lambda x, y: os.path.join(x,y)))
    for path in paths_to_check:
        if not os.path.exists(path):
            os.mkdir(path) 
    with open(abs_directory, 'w') as file_tgt:
        file_tgt.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
def dirs_to_cwd(file_path):
    """Takes file_path, and returns a list of top-down dirs to it"""
    dirs_to_filepath = []
    flag = True
    # Initialize with only directory names:
    split_result = os.path.split(os.path.dirname(file_path))
    while flag:
        if split_result[1] == '':
            flag = False
        else:
            dirs_to_filepath.append(split_result[1])
        split_result = os.path.split(split_result[0])
    #  Reverse list as it was taken from head to tail
    dirs_to_filepath = dirs_to_filepath[::-1]
    return dirs_to_filepath
