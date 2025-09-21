def main():
    AmountDue = 50

    while True:
        print("Amount Due:",AmountDue)
        InsertDue = int(input("Insert Coin: "))
        if InsertDue != 5 or InsertDue != 10 or InsertDue!= 25:
            AmountDue -= 0
        if InsertDue == 5:
            AmountDue -= 5
        elif InsertDue == 10:
            AmountDue -= 10
        elif InsertDue == 25:
            AmountDue -= 25

        if AmountDue <= 0:
            break

    print("Change Owed:",str(AmountDue).strip("-"))

main()
