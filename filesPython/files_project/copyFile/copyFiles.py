while True:
    user_input = input("Enter 3 friends names: ").strip().split(",")
    if len(user_input) == 3:
        break
    else:
        print("You should enter precisely 3 names, separated by a comma!")

friend_list = [name.strip() for name in user_input]

with open("people.txt", "r") as readable_file:
    people_data = [line.strip() for line in readable_file.readlines()]

friends_nearby_list = set(friend_list).intersection(people_data)
print(friends_nearby_list)

with open("nearby_friends.txt", "w") as writable_file:
    for friend in friends_nearby_list:
        writable_file.write(friend + "\n")
