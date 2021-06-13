from name_function import get_formatted_name

print("Enter 'q' to exit at any time")

while True:
    first = input("Enter first name: ")
    if first == 'q':
        break
    last = input("Enter last name: ")
    if first == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"Formatted name: {formatted_name}")
