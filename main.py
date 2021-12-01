# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
from dice import *
from player import *

import random
import time
import logging


def simulate_game(players, dices, field_length, bidding_simulation_round):
    """
    Simulate One Single Game
    :param players:                     the list of players from main driver
    :param dices:                       the list of dices from main driver
    :param field_length:                the length of the horse field
    :param bidding_simulation_round:    how many rounds do u want to simulate bidding
    :return:                            Statistics of this game
    """
    simulate_bidding(players, bidding_simulation_round)
    sort_players_on_bid_amount(players)

    for i, player in enumerate(players):
        logging.info('Players ' + str(i) + ' bids:' + str(player.bid_amount))

    #TODO: SET/DISTRIBUTE DICE/HORSE TO EACH PLAYER BASED ON THEIR ORDER IN LIST AND START GAME


def simulate_bidding(players, bidding_simulation_round):
    """
    Simulate Pre-Game Bidding, Random a Player to Bid higher than another Random Player's Bidding,
    Simulate n = bidding_simulation_round Rounds
    :param players:                     the list of players from main driver
    :param bidding_simulation_round:    how many rounds do u want to simulate
    :return:                            modifies players' bid amount
    """
    for i in range(bidding_simulation_round):
        # Find Someone that is not the highest bidder
        while True:
            bidding_person = players[random.randint(1, len(players) - 1)]
            if not is_largest_bidding_player(players, bidding_person):
                break
        higher_bidder = find_rand_player_with_more_bid(players, bidding_person)
        # Just bid 1 more
        bidding_person.increase_bid(higher_bidder.bid_amount - bidding_person.bid_amount + 1)


def sort_players_on_bid_amount(players: List[Player]):
    """
    Sort the players list based on their bidding amount
    :param players:     the list of players from main driver
    :return:            Sort the input list
    """
    players.sort(key=lambda x: x.bid_amount)


def is_largest_bidding_player(players: list, i_player: Player):
    """
    Check whether input player is the highest bidder
    :param players:     the list of players from main driver
    :param i_player:    input player
    :return:            True yes the player is the highest bidder, False otherwise
    """
    for player in players:
        if i_player.bid_amount < player.bid_amount:
            return False
    return True


def find_rand_player_with_more_bid(players: List[Player], i_player: Player):
    """
    Find a player with higher bid than input player randomly
    :param players:     the list of players from main driver
    :param i_player:    input player
    :return:            return the randomized player with higher bid
    """
    while True:
        logging.info('Finding Random Player with a bigger bid...')
        random_player = players[random.randint(1, len(players) - 1)]
        logging.info('Found Random Player with bid: ' + str(random_player.bid_amount))
        logging.info('Current Player has bid: ' + str(i_player.bid_amount))
        if random_player.bid_amount > i_player.bid_amount:
            return random_player
        else:
            logging.info('No match...')


def main():
    """
    Main Driver
    :return:
    """
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
        players.append(Player('Player ' + str(i), i + 1))

    simulate_game(players, dices, horse_field_len, bidding_simulation_round)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
