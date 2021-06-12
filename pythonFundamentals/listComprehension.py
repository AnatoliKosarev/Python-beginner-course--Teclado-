# can be used with lists, tuples, sets, dictionaries

numbers = [0, 1, 2, 3, 4]
doubled_numbers1 = []
for number in numbers:
    doubled_numbers1.append(number * 2)
print(doubled_numbers1)

# same can be done with list comprehension which is much shorter
doubled_numbers2 = [number2 * 2 for number2 in numbers]
print(doubled_numbers2)

doubled_numbers3 = [number3 * 2 for number3 in range(10)]
print(doubled_numbers3)

# we can reuse the base list
numbers = [number * 2 for number in numbers]
print(numbers)

friend_ages = [22, 35, 31, 27]
age_strings = [f"My friend is {age} years old" for age in friend_ages]
print(age_strings)

friend = input("Enter your friend's name: ")
names = ["Rolf", "Phil", "Vito"]
friends_lower = [name.lower() for name in names]
if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")

names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)
people = [(name.title(), age) for name, age in zip(names, ages)]
print(people)

# List comprehensions also allow for more than one for clause
# We can use this to find all the possible combinations of dice rolls for two dice, for example:
roll_combinations = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)] # for для d1 - внешний цикл, для d2 - внутренний
print(roll_combinations)

# dictionary comprehension
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")
students = {}
for student_id, name in zip(student_ids, names):
    student = {student_id: name.title()}
    students.update(student)
print(students)

students2 = {
    student_id: name.title() # the value we want to add to the new collection
    for student_id, name in zip(student_ids, names) # a loop definition which determines where the original values are coming from
}
print(students2)

students3 = {
    student_ids[i]: names[i].title() # the value we want to add to the new collection
    for i in range(len(student_ids)) # a loop definition which determines where the original values are coming from
}
print(students3)