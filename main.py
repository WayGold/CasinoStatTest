# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
from dice import *
from player import *

import random
import time
import logging


def simulate_once(players, dices, field_length, bidding_simulation_round):
    # Simulate Pre-Game Bidding, Random a Player to Bid higher than another Random Player's Bidding,
    # Simulate n = bidding_simulation_round Rounds
    for i in range(bidding_simulation_round):
        # Find Someone that is not the highest bidder
        while True:
            bidding_person = players[random.randint(1, len(players))]
            if not is_largest_bidding_player(players, bidding_person):
                break
        higher_bidder = find_rand_player_with_more_bid(players, bidding_person)
        # Just bid 1 more
        bidding_person.increase_bid(higher_bidder.bid_amount - bidding_person.bid_amount + 1)


def is_largest_bidding_player(players: list, i_player: Player):
    for player in players:
        if i_player.bid_amount <= player.bid_amount:
            return False
    return True


def find_rand_player_with_more_bid(players: List[Player], i_player: Player):
    while True:
        logging.info('Finding Random Player with a bigger bid...')
        random_player = players[random.randint(1, len(players))]
        if random_player.bid_amount > i_player.bid_amount:
            return random_player


def main():
    logging.getLogger().setLevel(logging.INFO)
    random.seed(time.time())

    horse_field_len = 50
    largest_dice_num = 20
    dice_decrement = 2
    bidding_simulation_round = 10

    players = []
    dices = []

    # Populate Dices/Horses and Players
    for i in range(5):
        dices.append(Dice(largest_dice_num - i * dice_decrement))
        players.append(Player('Player ' + str(i), i))

    simulate_once(players, dices, horse_field_len, bidding_simulation_round)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
