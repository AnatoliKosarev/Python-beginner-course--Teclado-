from HelloWorld.pythonTextBook.exercises.classes.exNineFive import User


class Admin(User):
    def __init__(self, first_name, last_name, middle_name=None, **user_info):
        super().__init__(first_name, last_name, middle_name=None, **user_info)
        self.rights = ["add user", "ban user", "delete user"]

    def show_rights(self):
        print(f"Admin rights: {', '.join(self.rights)}")


if __name__ == "__main":
    admin = Admin("Tom", "York")
    admin.show_rights()
    admin.describe_user()