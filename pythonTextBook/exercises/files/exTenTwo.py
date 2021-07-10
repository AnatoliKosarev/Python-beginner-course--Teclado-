def replace_value(filename, old_value, new_value):
    with open(filename, "r") as file:
        return [line.replace(old_value, new_value) for line in file.readlines()]


contents = replace_value("learning_python.txt", "Java", "Python3")
for cont_line in contents:
    print(cont_line.strip())
