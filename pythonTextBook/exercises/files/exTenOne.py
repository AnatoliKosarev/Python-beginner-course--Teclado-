def read_file_3_times(filename):
    with open(filename, "r") as file:
        print(file.read())

    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

    with open(filename, "r") as file:
        lines = file.readlines()
        return lines


contents = read_file_3_times("learning_python.txt")
for line in contents:
    print(line.strip())

