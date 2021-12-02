from dice import *


class Player:
    def __init__(self, i_name, i_bid_amount):
        self.bid_amount = i_bid_amount
        self.name = i_name
        self.dice = None
        self.current_distance_traveled = 0

    def get_bid_amount(self):
        return self.bid_amount

    def increase_bid(self, value):
        self.bid_amount += value

    def roll_dice(self):
        result = self.dice.rand_roll()
        self.current_distance_traveled += result
        return result

    def set_dice(self, i_dice: Dice):
        self.dice = i_dice
