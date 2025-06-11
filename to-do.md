# Project To Do after final submission

## Refactoring:
    refactor code in functions and create a single `scope_check` that can be utilized in all functions. Need to figure out this functions API (whether it returns only a False or also a path etc)

    Upon further research, we can utilize `os.path.commonpath(paths)`, more info can be found at [python docs](https://docs.python.org/3/library/os.path.html#os.path.basename)