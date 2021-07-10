def save_guest_name():
    name = input("Enter your name: ")
    if name:
        with open("guest.txt", "a") as f:
            f.write(f"{name}\n")


if __name__ == "__main__":
    save_guest_name()
