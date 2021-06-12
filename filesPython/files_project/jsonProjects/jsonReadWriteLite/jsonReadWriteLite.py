import json

cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Ford", "model": "Focus"}
]


def write_to_file(file_name, output):
    with open(file_name, "w") as f:
        json.dump(output, f)


def read_from_file(file_name):
    with open(file_name, "r") as f:
        file_contents = json.load(f) # reads file and turns it to dictionary
    print(file_contents)


write_to_file("cars_json.json", cars)
read_from_file("cars_json.json")

json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
dict_car = json.loads(json_string) # loads() turns json string into a dictionary, dumps() turns dictionary into a json string
print(dict_car)
print(dict_car[0]["name"])