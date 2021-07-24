from HelloWorld.advancedOOP.adv_oop_project.admin import Admin
from HelloWorld.advancedOOP.adv_oop_project.user import User
from HelloWorld.advancedOOP.adv_oop_project.database import Database

a = Admin('rolf', '1234', '3')
u = User('jose', 'password')


users = [a, u]
for user in users:
    user.save()

print(Database.find(lambda x: x['username'] == 'rolf'))
print(Database.find(lambda x: x['password'] == 'password'))
print(Database.content['users'])

Database.remove(lambda x: x['username'] == 'jose')
print(Database.content['users'])
