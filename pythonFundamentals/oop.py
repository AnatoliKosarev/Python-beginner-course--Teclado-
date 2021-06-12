my_student = {
    "name": "Rolf Smith",
    "grades": [70, 88, 90, 99]
}


def count_avg(grades):
    return sum(grades) / len(grades)


print(count_avg(my_student["grades"]))


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade_count(self):
        print(f"{self.name} with average grade {sum(self.grades) / len(self.grades)}")


student = Student("Rolf Smith", [70, 88, 90, 99])

student.average_grade_count() # 1 way to call a method (same object on which the method is called)
Student.average_grade_count(student) # 2 way to call a method (the object is passed as an argument)
print(student.grades)