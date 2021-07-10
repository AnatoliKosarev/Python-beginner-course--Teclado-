def sum_and_save():
    value1 = input("Enter first value: ")
    value2 = input("Enter second value: ")
    try:
        formatted_value1 = int(value1)
        formatted_value2 = int(value2)
    except ValueError as ex:
        print(f"Entered value of incorrect format: {ex}")
    else:
        print(f"Sum results: {formatted_value1 + formatted_value2}")


sum_and_save()