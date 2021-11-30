import dice


class Player:
    def __init__(self, i_name, i_bid_amount, i_dice: dice.Dice):
        self.bid_amount = i_bid_amount
        self.name = i_name
        self.dice = i_dice

    def get_bid_amount(self):
        return self.bid_amount

    def increase_bid(self, value):
        self.bid_amount += value

    def roll_dice(self):
        return self.dice.rand_roll()
