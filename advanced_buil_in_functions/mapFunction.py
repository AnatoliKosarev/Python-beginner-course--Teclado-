friends = ["Rolf", "Anna", "Randy", "Bob"]

friends_lower = map(lambda friend: friend.lower(), friends)
friends_lower = [friend.lower() for friend in friends]
friends_lower = (friend.lower() for friend in friends)  # generator comprehension should be used more
