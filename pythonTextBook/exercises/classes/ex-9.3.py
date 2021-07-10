class User:
    def __init__(self, first_name, last_name, middle_name=None, **user_info):
        self.user_info = user_info
        self.user_info["first_name"] = first_name
        self.user_info["last_name"] = last_name
        self.user_info["middle_name"] = middle_name

    def describe_user(self):
        for k, v in self.user_info.items():
            if v:
                print(f"{k}: {v}")

    def greet(self):
        if self.user_info["middle_name"]:
            full_name = f"{self.user_info['first_name']} {self.user_info['middle_name']} {self.user_info['last_name']}"
        else:
            full_name = f"{self.user_info['first_name']} {self.user_info['last_name']}"
        print(f"Hello, {full_name}")


user = User("Mike", "Smith", "J", birth="26.02.1984", last_login="12.01.2021")
user.describe_user()
user.greet()

user2 = User("Kollin", "Farrel", last_login="01.04.2021")
user2.describe_user()
user2.greet()