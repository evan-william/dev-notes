import sys
import csv
from tabulate import tabulate

if len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 2:
    try:
        if "." in sys.argv[1]:
            word, format = sys.argv[1].rsplit(".", 1)
            if format == "csv":
                try:
                    with open(sys.argv[1], 'r') as file:
                        reader = csv.reader(file)
                        table = []
                        headers = list(next(reader))
                        for row in reader:
                            table.append(row)
                    print(tabulate(table, headers, tablefmt="grid"))
                except FileNotFoundError:
                    sys.exit("File does not exist")
            else:
                sys.exit("Not a CSV file")
        else:
            sys.exit("Not a CSV file")
    except IndexError:
        sys.exit("Not a CSV file")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
