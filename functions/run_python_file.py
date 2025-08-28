import os
import subprocess
import time

def run_python_file(working_directory, file_path, args=[]):
    abs_wd = os.path.abspath(working_directory)
    abs_fp = os.path.abspath(os.path.join(abs_wd, file_path))
    print(f'abs_wd = {abs_wd}\nabs_fp = {abs_fp}')

    # Error and Restriction handling
    if not abs_fp.startswith(abs_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_fp):
        return f'Error: File "{file_path}" not found.'
    if abs_fp[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'

    seconds_now = time.time() - 1
    while True:
        run_args = ['python3', abs_fp] + args
        output = subprocess.run(run_args, capture_output=True)
        stderr = output.stderr.decode("utf-8")
        stdout = output.stdout.decode("utf-8")
        exit_code = output.returncode
        
        return_str = f'STDOUT:\n{stdout}\nSTDERR:{stderr}'
        if not output:
            return "No output produced."
        if exit_code:
            return f'Process exited with code {exit_code}\n{return_str}'
        else:
            return return_str

        # Exit loop:
        if time.time() - seconds_now > 30:
            break


