import sys
from PIL import Image, ImageOps

if len(sys.argv) >= 4:  # Check if something comes after scourgify.py 3 TIMES
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 3:  # Check if something comes after scourgify.py ONCE (THIS MAIN FUNCTION)
    try:
        if "." in sys.argv[1] and "." in sys.argv[2]:
            word1, format1 = sys.argv[1].rsplit(".", 1)  # Split from the right
            word2, format2 = sys.argv[2].rsplit(".", 1)  # Split from the right
            if format1 == "jpg" and format2 == "jpg":  # CHECK IF IT'S FORMATTED AS CSV
                try:
                    shirt = Image.open("shirt.png")
                    input_image = Image.open(sys.argv[1])

                    # Resize and crop input to match the shirt's size
                    input_image = ImageOps.fit(input_image, shirt.size)

                    # Overlay the shirt on the input image
                    input_image.paste(shirt, shirt)

                    # Save the output , THIS ONE WILL AUTO CREATE 2nd ARG
                    input_image.save(sys.argv[2])
                except FileNotFoundError:  # IF NOT FOUND
                    sys.exit(f"Could not open {sys.argv[1]}")
            elif format1 == "jpg" and format2 != "jpg":
                sys.exit("Input and output have different extensions")
            elif format1 != "jpg" and format2 == "jpg":
                sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid Input")
        else:
            sys.exit("Invalid Input")
    except IndexError:
        sys.exit("Invalid Input")

elif len(sys.argv) <= 2:  # Quit when nothing comes after scourgify.py + x [0]
    sys.exit("Too few command-line arguments")

