from sys import argv
from sys import exit

if len(argv) > 1:
    args = argv[1:]
else:
    print("error")
    exit(1)

print(args)
