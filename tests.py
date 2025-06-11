import sys
from functions.get_files_info import get_files_info
from functions.get_files_content import get_files_content
from functions.write_file import write_file

# overriding bootdev's testing:
if len(sys.argv) < 2:
    sys.argv.append("write")

if sys.argv[1] == "info":
    print("Testing calculator and '.':")
    print(get_files_info('./calculator', '.'))
    print ("\n")

    print("Testing calculator and pkg")
    print(get_files_info('./calculator', 'pkg'))
    print ("\n")

    print("Testing calculator and /bin")
    print(get_files_info('./calculator', '/bin'))
    print ("\n")

    print("Testing calculator and ../")
    print(get_files_info('calculator', '../'))
    print ("\n")

if sys.argv[1] == "content":
    print("Testing calculator and 'lorem':")
    print(get_files_content('calculator', 'lorem.txt')[-60:])
    print ("\n")

    print("Testing calculator and 'main.py':")
    print(get_files_content('calculator', 'main.py'))
    print ("\n")

    print("Testing calculator and 'pkg/calculator.py':")
    print(get_files_content('calculator', 'pkg/calculator.py'))
    print ("\n")

    print("Testing calculator and '/bin/cat':")
    print(get_files_content('calculator', '/bin/cat'))
    print ("\n")

if sys.argv[1] == "write":
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
