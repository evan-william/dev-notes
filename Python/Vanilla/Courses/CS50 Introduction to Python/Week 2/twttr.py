def main():
    Input = input("Input: ").strip()
    Output = ""

    for char in Input:
            Output += char.strip('aeiuoAEIUO')

    print("Output:",Output,end="")
    print()

main()
