def interact():
    while True:
        try:
            user_input = int(input("Please input an integer:"))
        except ValueError:
            print("Please input integers only.")
        else:
            is_even = user_input % 2 == 0
            print("{} is {}".format(user_input, "even" if is_even else "odd"))
        finally:
            user_input = input("Do you want to play again? (y/N):")
            if user_input != "y":
                print("Goodbye.")
                break

interact()