class User:
    def __init__(self, first_name, last_name, middle_name=None, **user_info):
        self.user_info = user_info
        self.user_info["first_name"] = first_name
        self.user_info["last_name"] = last_name
        self.user_info["middle_name"] = middle_name
        self.user_info["login_attempts"] = 0

    def increment_login_attempts(self):
        self.user_info["login_attempts"] += 1

    def reset_login_attempts(self):
        self.user_info["login_attempts"] = 0

    def describe_user(self):
        for k, v in self.user_info.items():
            if v or v == 0:
                print(f"{k}: {v}")

    def greet(self):
        if self.user_info["middle_name"]:
            full_name = f"{self.user_info['first_name']} {self.user_info['middle_name']} {self.user_info['last_name']}"
        else:
            full_name = f"{self.user_info['first_name']} {self.user_info['last_name']}"
        print(f"Hello, {full_name}")


if __name__ == "__main__":
    user = User("Tom", "John")
    print(user.user_info["login_attempts"])
    user.describe_user()
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()
    print(user.user_info["login_attempts"])
    user.describe_user()
    user.reset_login_attempts()
    print(user.user_info["login_attempts"])
    user.describe_user()