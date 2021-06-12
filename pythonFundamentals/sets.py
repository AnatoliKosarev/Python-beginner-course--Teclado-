# no order, no duplicate values
art_friends = set()
art_friends = {"tom", "jane"}
print(art_friends)

art_friends.add("jen")
print(art_friends)

art_friends.add("jen")
print(art_friends)

extra_art_friends = ["kim", "lan"]
art_friends.update(extra_art_friends)
print(art_friends)

# throws key error if specified element not found in set
art_friends.remove("jen")
print(art_friends)

# doesn't throw key error if specified element not found in set
art_friends.discard("jen")
print(art_friends)

# removes some random value
art_friends.pop()
print(art_friends)

art_friends.clear()
print(art_friends)

art_friends = {"tom", "jane", "bruce"}
other_friends_list = ["bob", "bill"]
all_art_friends = art_friends.union(other_friends_list)
print(all_art_friends)
science_friends = {"bruce", "clint", "tom", "tom"}
all_friends = all_art_friends.union(science_friends) # same as all_friends = all_art_friends | science_friends
print(all_friends)

common_friends = all_art_friends.intersection(science_friends) # same as common_friends = all_art_friends & science_friends
print(common_friends)

print(all_art_friends.difference(science_friends)) # same as all_art_friends - science_friends
print(science_friends.difference(all_art_friends))

print(all_art_friends.symmetric_difference(science_friends)) # same as all_art_friends ^ science_friends
print(science_friends.symmetric_difference(all_art_friends))

print(len(all_art_friends))

print("bob" in all_art_friends)