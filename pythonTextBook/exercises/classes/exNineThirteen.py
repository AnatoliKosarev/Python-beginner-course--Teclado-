from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))


if __name__ == "__main__":
    dice = Dice()
    dice.roll_dice()
    dice.roll_dice()
    dice.roll_dice()
    dice.roll_dice()
    dice.roll_dice()
    dice.roll_dice()
    dice.roll_dice()
    dice.roll_dice()
    dice.roll_dice()
    dice.roll_dice()
    print()
    dice10 = Dice(10)
    dice10.roll_dice()
    dice10.roll_dice()
    dice10.roll_dice()
    dice10.roll_dice()
    dice10.roll_dice()
    dice10.roll_dice()
    dice10.roll_dice()
    dice10.roll_dice()
    dice10.roll_dice()
    dice10.roll_dice()
    print()
    dice20 = Dice(20)
    dice20.roll_dice()
    dice20.roll_dice()
    dice20.roll_dice()
    dice20.roll_dice()
    dice20.roll_dice()
    dice20.roll_dice()
    dice20.roll_dice()
    dice20.roll_dice()
    dice20.roll_dice()
    dice20.roll_dice()
