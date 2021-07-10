class Privileges:
    def __init__(self):
        self.rights = ["add user", "ban user", "delete users"]

    def show_rights(self):
        print(f"Admin rights: {', '.join(self.rights)}")