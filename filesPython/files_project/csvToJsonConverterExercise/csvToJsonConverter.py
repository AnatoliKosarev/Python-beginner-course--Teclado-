import csv
import json


def read_csv_file(file_name):
    with open(file_name, "r") as csv_file:
        return list(csv.DictReader(csv_file, fieldnames=["club", "city", "country"]))


def write_to_json_file(file_name, output):
    with open(file_name, "w") as file:
        json.dump(output, file)


csv_contents = read_csv_file("csv_file.txt")
write_to_json_file("json_file.txt", csv_contents)
