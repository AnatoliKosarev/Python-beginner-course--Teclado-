import csv
import json


def read_csv_file(file_name):
    with open(file_name, "r") as csv_file:
        return list(csv.DictReader(csv_file, fieldnames=["club", "city", "country"]))


def write_to_json_file(file_name, output):
    with open(file_name, "w") as file:
        json.dump(output, file)


def read_json(name):
    with open(name, 'r') as f:
        return json.load(f)


def write_csv(name, output):
    with open(name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)


# csv_contents = read_csv_file("csv_file.txt")
# write_to_json_file("json_file.txt", csv_contents)

json_contents = read_json("json_file.txt")
write_csv("csv_file.txt", json_contents)