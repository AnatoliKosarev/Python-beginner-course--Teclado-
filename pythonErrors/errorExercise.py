def the_power_of_two():
    user_input = input("Enter number:")
    try:
        number = float(user_input)
    except ValueError:
        print("Your input is invalid. Using 0 as default.")
        return 0
    else:
        n_square = number ** 2
        return n_square

print(the_power_of_two())