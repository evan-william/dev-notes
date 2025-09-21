def main():
    tempo = 0
    Total = 0

    foodlist = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    while True:
        try:
            food = input("Item: ").title().strip()
            if food in foodlist:
                tempo = foodlist[food]
                Total += tempo
                print(f"Total: ${Total:.2f}")
        except EOFError:
            print()
            break

main()








