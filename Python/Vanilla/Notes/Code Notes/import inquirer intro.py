import inquirer

questions = [
    inquirer.List(
        "choice",
        message="What do you want to do?",
        choices=["Register", "Login", "Exit"],
    )
]

answer = inquirer.prompt(questions)
print(f"You selected: {answer['choice']}")

"""
def main():
    while True:
        clear_screen()
        print(menu())
        questions = [
            inquirer.List(
                "choice",
                message="Choose an option",
                choices=["Register", "Login", "Exit"]
            )
        ]
        answer = inquirer.prompt(questions)
        if answer["choice"] == "Register":
            startregister()
        elif answer["choice"] == "Login":
            startlogin()
        else:
            print("Exiting game...")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
"""