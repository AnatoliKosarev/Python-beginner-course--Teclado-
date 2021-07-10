def read_files(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    read_files("cat_names.txt")
    read_files("dog_names.txt")