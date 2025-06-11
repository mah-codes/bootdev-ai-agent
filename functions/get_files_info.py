import os

def get_files_info(working_directory, directory=None):
    out_of_scope = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    pwd = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    if  pwd != abs_directory[:len(pwd)]:
        return out_of_scope
    elif not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    
    dirs = os.scandir(abs_directory)
    output = []
    for dir in dirs:
        try:
            f_name = os.path.basename(dir.path)
            f_size = os.path.getsize(dir.path)
            f_isdir = dir.is_dir()
            output.append(f'{f_name}: file_size={f_size} bytes, is_dir={f_isdir}')
        except Exception as e:
            return f'Error: {e}'
    return "\n".join(output)

    
    
    