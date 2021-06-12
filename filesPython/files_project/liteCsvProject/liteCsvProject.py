with open('csv_data.csv', 'r') as readable_file:
    file_data = readable_file.readlines()

data_list = [line.strip() for line in file_data[1:]]

for line in data_list:
    name, age, university, degree = line.split(",")
    print(f'{name.title()} is {age}, studying {degree.capitalize()} at {university.title()}')


sample_csv_value = ','.join(['john', '25', 'LIO', 'Sports'])
with open('csv_data.csv', 'a') as writable_file:
    writable_file.write('\n' + sample_csv_value)