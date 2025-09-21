number = input("Enter the number = ").strip()
match number:
    case "42" | "Forty Two" | "forty-two" | "forty two" | "FoRty TwO":
        print("Yes")
    case _:
        print("No")
