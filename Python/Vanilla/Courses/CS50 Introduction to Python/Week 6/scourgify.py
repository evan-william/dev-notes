import sys
import csv

if len(sys.argv) >= 4:  # Check if something comes after scourgify.py 3 TIMES
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 3:  # Check if something comes after scourgify.py ONCE (THIS MAIN FUNCTION)
    try:
        if "." in sys.argv[1]:
            word, format = sys.argv[1].rsplit(".", 1)  # Split from the right
            if format == "csv":  # CHECK IF IT'S FORMATTED AS CSV
                try:
                    with open(sys.argv[1], "r", newline="") as input_file:
                        reader = csv.DictReader(input_file)  # Read CSV as dictionary

                        with open(sys.argv[2], "w", newline="") as output_file:
                            fieldnames = ["first", "last", "house"]
                            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                            writer.writeheader()

                            for row in reader:
                                last, first = row["name"].split(", ")
                                writer.writerow({"first": first, "last": last, "house": row["house"]})

                except FileNotFoundError:  # IF NOT FOUND
                    sys.exit(f"Could not read {sys.argv[1]}")
            else:
                sys.exit("Not a CSV file")
        else:
            sys.exit("Not a CSV  file")
    except IndexError:
        sys.exit("Not a CSV file")

elif len(sys.argv) <= 2:  # Quit when nothing comes after scourgify.py + x [0]
    sys.exit("Too few command-line arguments")
