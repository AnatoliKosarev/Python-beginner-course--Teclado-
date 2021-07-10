from HelloWorld.pythonTextBook.exercises.classes.exNineEight import User, Privileges, Admin

admin = Admin("Tom", "York", location="Oxford")
admin.rights.show_rights()

user = User("Mike", "Staff")
user.greet()