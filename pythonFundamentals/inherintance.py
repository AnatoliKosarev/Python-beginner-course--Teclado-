class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @property
    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student): # extends Student
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    # @property decorator converts method into property - applicable for methods that don't perform any actions -
    # just return a value e.g., and don't have arguments. After that such methods can be called without ()
    @property
    def weekly_salary(self):
        return self.salary * 37.5


rolf = WorkingStudent("Rolf", "MIT", 15.50)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average)
print(rolf.weekly_salary)