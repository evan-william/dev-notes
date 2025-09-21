def detector():
    x, y, z = number.split(" ")

    if y == "+":
        total = int(x) + int(z)
        print(f"{total:.1f}")
    elif y == "-":
        total = int(x) - int(z)
        print(f"{total:.1f}")
    elif y == "*":
        total = int(x) * int(z)
        print(f"{total:.1f}")
    elif y =="/":
        total = int(x) / int(z)
        print(f"{total:.1f}")

number = input("Expression: ")
detector()

