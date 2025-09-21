import validators

def main():
    email = input("Email: ").strip()  # Prompt user for input and remove any leading/trailing spaces
    if validators.email(email):  # Check if the email is valid
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

