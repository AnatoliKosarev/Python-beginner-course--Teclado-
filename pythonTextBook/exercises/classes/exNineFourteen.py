from random import choice


class Lottery:
    def __init__(self, lottery_list):
        self.lottery_list = lottery_list

    def run_lottery(self):
        winning_value_list = []
        lottery_list_copy = self.lottery_list[:]
        while len(winning_value_list) < 4:
            winning_value = choice(lottery_list_copy)
            lottery_list_copy.remove(winning_value)
            winning_value_list.append(winning_value)
        print(f"Winning values are: {', '.join(winning_value_list)}.")
        return winning_value_list

    def analyze_lottery_result(self, winning_values):
        if winning_values:
            generated_winning_list = []
            counter = 0
            while generated_winning_list != winning_values:
                generated_winning_list = self.run_lottery()
                counter += 1
            print(f"It took {counter} iterations to generate original results.")


lottery_to_run = ["a", "1", "41", "e", "q", "35", "87", "96", "2", "l", "85", "9", "11", "32", "t"]
lottery = Lottery(lottery_to_run)
wins = lottery.run_lottery()
lottery.analyze_lottery_result(wins)
