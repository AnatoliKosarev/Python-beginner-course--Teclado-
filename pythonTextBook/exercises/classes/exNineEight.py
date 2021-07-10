from HelloWorld.pythonTextBook.exercises.classes.exNineFive import User
from HelloWorld.pythonTextBook.exercises.classes.privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, middle_name=None, **user_info):
        super().__init__(first_name, last_name, middle_name=None, **user_info)
        self.rights = Privileges()


if __name__ == "__main__":
    admin = Admin("Tom", "York")
    admin.rights.show_rights()
    admin.describe_user()