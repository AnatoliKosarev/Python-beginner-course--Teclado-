while True:
    age = input("Enter your age: ")
    try:
        age = int(age)
    except ValueError:
        print("Invalid value entered")
    else:
        if 0 <= age < 3:
            print("Free ticket")
            break
        elif 3 <= age < 12:
            print("Ticket costs 10$")
            break
        elif age >= 12:
            print("Ticket costs 15$")
            break
        else:
            print("Enter value larger than 0")