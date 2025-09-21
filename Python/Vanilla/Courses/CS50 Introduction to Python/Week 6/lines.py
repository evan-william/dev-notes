import sys
import string

if len(sys.argv) >= 3: # Check if something comes after lines.py TWICE
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 2: # Check if something comes after lines.py ONCE (THIS MAIN FUNCTION)
    try:
        if "." in sys.argv[1]:
             word, format = sys.argv[1].rsplit(".", 1)  # Split from the right
             if format == "py": # CHECK IF ITS FORMATTED AS PY
                try:
                    count = 0
                    with open(sys.argv[1]) as filecheck:
                        for lines in filecheck: # CHECK THE LINE HOW MANY
                            lines = lines.strip()
                            if lines and not lines.startswith("#"):
                                 count += 1
                    print(count)
                except FileNotFoundError: # IF NOT FOUND
                    sys.exit("File does not exist")
             else:
                sys.exit("Not a Python file")
        else:
             print("Not a Python file")
    except IndexError:
        sys.exit("Not a python file")

elif len(sys.argv) == 1: # Quit when nothing comes after lines.py
    sys.exit("Too few command-line arguments")

