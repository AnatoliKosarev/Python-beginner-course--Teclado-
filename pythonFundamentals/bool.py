age = int(input("enter your age: "))
side_job = False
print(age > 18 and age < 65 or side_job) # When it comes to Boolean operators, not is the most important.
# This always gets evaluated first. Then and operations are evaluated, and finally or.
print(side_job or age > 18 and age < 65)