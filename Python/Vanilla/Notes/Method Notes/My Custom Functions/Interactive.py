import inquirer

# 1. Interactive Inquirer
while True:
        # clear_screen()
        # print(menu())
        questions = [
            inquirer.List(
                "choice",
                message="Choose an option",
                choices=["1. Generate Quote", "2. Show Saved Quote", "3. Exit"]
            )
        ]

        answer = inquirer.prompt(questions)
        if answer["choice"] == "1. Generate Quote":
            ...
        elif answer["choice"] == "2. Show Saved Quote":
            ...
        else:
            ...
            # dot_generate("Exiting")
            # sys.exit(0)

