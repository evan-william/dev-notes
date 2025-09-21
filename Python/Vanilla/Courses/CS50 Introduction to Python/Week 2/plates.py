import string

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(check):
    if not (2 <= len(check) <= 6) and not check[0:2].isalpha():
        return False

    digit_found = False

    for char in check:
        if char.isdigit():
            if char == "0" and not digit_found:
                return False
            digit_found = True
        elif digit_found:
            return False

    for char in check:
        if char in string.punctuation:
            return False

    return True

main()
