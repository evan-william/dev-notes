import sys
import random
from pyfiglet import Figlet

def main():
    output = Figlet()

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        if sys.argv[2] not in output.getFonts():
            sys.exit("Invalid font name")

        output.setFont(font=sys.argv[2])

    elif len(sys.argv) == 1:
        output.setFont(font=random.choice(output.getFonts()))

    else:
        sys.exit("Invalid usage")

    text_input = input("Input: ")

    print("Output:")
    print(output.renderText(text_input))

main()
