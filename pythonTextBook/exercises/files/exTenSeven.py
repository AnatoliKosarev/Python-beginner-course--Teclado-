def sum_and_save():
    sum_list = []
    value = input("Enter value, 'r' to see result, 'q' to exit: ")
    while value != "q" and value != "r":
        try:
            formatted_value = int(value)
        except ValueError:
            print(f"Entered value is of incorrect format: {value}")
        else:
            sum_list.append(formatted_value)
        value = input("Enter value, 'r' to see result, 'q' to exit: ")
    if value == "r" and sum_list:
        print(f"Sum result: {sum(sum_list)}")


if __name__ == "__main__":
    sum_and_save()