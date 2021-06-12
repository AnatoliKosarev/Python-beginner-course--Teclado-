import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

winning_player = players[0]
numbers_matched = 0

for player in players:
    numbers_matched = len(player.get("numbers").intersection(lottery_numbers))
    if numbers_matched > len(winning_player.get("numbers").intersection(lottery_numbers)):
        winning_player = player

if numbers_matched > 0:
    winnings = 100 ** numbers_matched
    print(f"{winning_player.get('name')} won {winnings}")
else:
    print(f"Nobody one,{numbers_matched} numbers were matched")

print(lottery_numbers)
print(winning_player.get("numbers"))
print(numbers_matched)

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)