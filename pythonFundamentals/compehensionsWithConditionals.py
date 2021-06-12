ages = [22, 35, 21, 20, 36]
odds = [age for age in ages if age % 2 == 0]
print(odds)
# [22, 20, 36]

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "rolf", "Charlie", "Mike"]
friends_lower = [friend.lower() for friend in friends]
present_friends = [
    name.title()
    for name in guests
    if name.lower() in friends_lower # can be done as <if name.lower() in [friend.lower() for friend in friends]> but it becomes unreadable
]
print(present_friends)
# ['Rolf', 'Charlie']

names = ["Matthew", "John", "Helen", "Stephen", "Alexandra", "Rolf"]
short_final_n = [name for name in names if len(name) < 6 if name[-1] == "n"]
print(short_final_n)
# ['John', 'Helen']