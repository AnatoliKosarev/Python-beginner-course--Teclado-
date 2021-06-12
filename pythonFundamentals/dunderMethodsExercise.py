class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __str__(self):
        return f"Club {self.name} with {len(self.players)} players"

    def __repr__(self):
        return f"Club {self.name}: {self.players}"

    def __getitem__(self, item):
        if isinstance(item, int):
            if item < 0:
                item = len(self.players) + item
            if item < 0 or item >= len(self.players):
                raise IndexError("Club index is out of range")
            else:
                return self.players[item]
        elif isinstance(item, slice):
            start, stop, step = item.indices(len(self.players))
            rng = range(start, stop, step)
            return [self.players[index] for index in rng]
        else:
            invalid_type = type(item)
            raise TypeError("Index should be of type int, not {}".format(invalid_type.__name__))


club = Club("Arsenal")
print(club.name)

club.players.append("Henry")
club.players.append("Fabregas")
club.players.append("Robbinson")
club.players.append("Ljungberg")
print(club.players)

print(club[-1])
players_part = club[0::2]
print(players_part)

for player in club.players:
    print(player)

print(club)
print(club.__repr__())