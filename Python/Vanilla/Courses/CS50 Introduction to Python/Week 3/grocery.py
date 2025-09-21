def main():
    dict = {}

    while True:
        try:
            addlist = input("").strip().upper()
            if addlist in dict:
                dict[addlist] += 1
            else:
                dict[addlist] = 1

        except EOFError:
            print()
            for item in sorted(dict.keys()):  # Sorting keys alphabetically
                print(f"{dict[item]} {item}")
            break

main()
