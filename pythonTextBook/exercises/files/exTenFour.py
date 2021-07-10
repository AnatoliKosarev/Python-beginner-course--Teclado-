def greet_guest():
    name = input("Enter name or 'q' to exit: ")
    while name != "q":
        if name:
            greeting = f"Welcome, {name}!"
            print(greeting)
            with open("guest_book.txt", "a") as f:
                f.write(f"{greeting}\n")
        name = input("Enter name or 'q' to exit: ")


if __name__ == "__main__":
    greet_guest()
