from HelloWorld.advancedOOP.adv_oop_project.saveable import Saveable


class User(Saveable):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print('You are logged in!')

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }
