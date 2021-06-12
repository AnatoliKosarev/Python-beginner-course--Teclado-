from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "faculty"])

names = ["John", "Steve", "Mary"]
ages = [19, 20, 18]
faculties = ["Politics", "Economics", "Engineering"]

students = [
    Student(*student_data)
    for student_data in zip(names, ages, faculties)
]

print(students)

oldest_student = max(students, key=lambda student: student.age)
# In the code above, we've set a custom key for max so that it compares our tuples based on the age element in each tuple
print(oldest_student)