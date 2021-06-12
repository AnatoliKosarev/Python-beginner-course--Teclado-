lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        "name": "John Smith",
        "numbers": {22, 100, 5, 10, 2}
    },
    {
        "name": "Mike Kelly",
        "numbers": {20, 101, 52, 19, 21}
    }
]

message = "Player {player_name} got {correct_numbers_quantity} numbers right"

'''
for player in players:
    player_name = ""
    correct_numbers_quantity = 0
    for key, value in player.items():
        if key == "name":
            player_name = value
        if key == "numbers":
            correct_numbers_quantity = len(value.intersection(lottery_numbers))
    print(message.format(player_name=player_name, correct_numbers_quantity=correct_numbers_quantity))
    '''

for player in players:
    player_name = player.get("name", "Unknown") # player_name = player["name"]
    correct_numbers_quantity = len(player.get("numbers", set()).intersection(lottery_numbers))
    #print(message.format(player_name=player_name, correct_numbers_quantity=correct_numbers_quantity))
    print(f"Player {player_name} got {correct_numbers_quantity} numbers right")