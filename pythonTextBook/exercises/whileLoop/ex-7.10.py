responses = {}

polling_active = True

while polling_active:
    name = input("Enter your name: ")
    response = input("Where would you like to go for a vacation: ")
    responses[name] = response
    while True:
        repeat = input("Would you like continue polling (yes / no): ")
        if repeat == "yes":
            break
        elif repeat == "no":
            for name, response in responses.items():
                print(f"{name.title()}'s response: {response}.")
            polling_active = False
            break
        else:
            print("Invalid entry, try again.")