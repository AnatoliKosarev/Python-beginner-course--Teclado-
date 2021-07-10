import csv

movies = [
    {'name': 'The Matrix', 'director': 'Wachowski'},
    {'name': 'Green Book', 'director': 'Farrelly'},
    {'name': 'Amadeus', 'director': 'Forman'}
]

"""
BASE IMPLEMENTATION WITH LIMITATIONS
def write_to_file(output):
    with open('file_to_write_to.csv', 'w') as writable_file:
        writable_file.write(','.join(['name', 'director\n']))
        for line in output:
            writable_file.write(f"{line['name']},{line['director']}\n")


def read_from_file(file_name):
    try:
        with open(file_name, 'r') as readable_file:
            content = readable_file.readlines()

    except FileNotFoundError:
        print(f"{file_name} file is not found.")

    else:
        for line in content[1:]:
            columns = line.strip().split(',')
            print(f"Name: {columns[0]}\tDirector: {columns[1]}")


write_to_file(movies)
read_from_file('file_to_write_to.csv')
"""

"""
IMPLEMENTATION WITH CSV MODULE WITH INCORRECT HEADER READ FROM FILE


def write_to_file(file_name, output):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        f.write('name,director\n')
        writer.writerows([elem.values() for elem in output])


def read_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                print(f"Name: {line[0]}\tDirector: {line[1]}")
    except FileNotFoundError:
        print(f"{file_name} file is not found.")


write_to_file('file_to_write_to.csv', movies)
read_from_file('file_to_write_to.csv')

Name: name	Director: director
Name: The Matrix	Director: Wachowski
Name: Green Book	Director: Farrelly
Name: Amadeus	Director: Forman
"""

"""
DICTREADER CAN BE USED IF DICTIONARY IS USED AS DATA SOURCE TYPE
"""


def write_to_file(file_name, output):
    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(output[0].keys())) # передаем ключи словаря для того чтобы печатать заголовок
        writer.writeheader() # Write a row with the field names (as specified in the constructor). не будет печатать заголовок при выводе на экран, т.к. будет знать что это заголовок
        writer.writerows(output)

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            reader = csv.DictReader(f)
            # keys = reader.fieldnames
            # for line in reader:
            #     print(f"Name: {line[keys[0]]}\tDirector: {line[keys[1]]}")
            return list(reader)

    except FileNotFoundError:
        print(f"{file_name} file is not found.")


write_to_file('file_to_write_to.csv', movies)
result = read_from_file('file_to_write_to.csv')
print(result)