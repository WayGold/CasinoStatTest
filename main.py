# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List, Dict
from player import *

import random
import time
import logging


def simulate_game(players, dices: List[Dice], field_length, bidding_simulation_round, start_modifiers):
    """
    Simulate One Single Game
    :param players:                     the list of players from main driver
    :param dices:                       the list of dices from main driver
    :param field_length:                the length of the horse field
    :param bidding_simulation_round:    how many rounds do u want to simulate bidding
    :param start_modifiers:             high bidders get a head start on the race
    :return:                            Statistics of this game
    """
    simulate_bidding(players, bidding_simulation_round)
    sort_players_on_bid_amount(players)

    for i, player in enumerate(players):
        logging.debug('Players ' + player.name + ' bids:' + str(player.bid_amount))
        player.set_dice(dices[i])
        player.current_distance_traveled += start_modifiers[i]
        player.bid_rank = 5 - i

    for player in players:
        logging.debug('Players ' + player.name + ' with Dice:' + str(player.dice.d_num))

    # Start Game - Roll Dices
    while True:
        break_outer = False
        # Keep Rolling Dices for each player
        for player in players:
            player.roll_dice()
            # Check for win
            if player.current_distance_traveled >= field_length:
                break_outer = True
                break
        if break_outer:
            break

    log_summary_of_game(players)
    winner_bid_rank = log_winner_of_game(players, field_length).bid_rank
    return winner_bid_rank


def log_summary_of_game(players: List[Player]):
    for player in players:
        logging.debug('Players ' + player.name + ' with Distance Traveled:' + str(player.current_distance_traveled))


def log_winner_of_game(players: List[Player], field_length):
    for player in players:
        if player.current_distance_traveled >= field_length:
            logging.debug('Winner is ' + player.name + ' with Distance Traveled:' +
                          str(player.current_distance_traveled))
            return player


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
    players.sort(key=lambda x: x.bid_amount, reverse=True)


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
        logging.debug('Finding Random Player with a bigger bid...')
        random_player = players[random.randint(1, len(players) - 1)]
        logging.debug('Found Random Player with bid: ' + str(random_player.bid_amount))
        logging.debug('Current Player has bid: ' + str(i_player.bid_amount))
        if random_player.bid_amount > i_player.bid_amount:
            return random_player
        else:
            logging.debug('No match...')


def re_init_players(players):
    players.clear()
    for i in range(5):
        players.append(Player('Player ' + str(i), i + 1))


def log_stats(winner_bid_rank_map: Dict[int, int], total_simulation):
    logging.info('Win Percentage Stats: ')
    for key, value in winner_bid_rank_map.items():
        if key == 5:
            logging.info('Highest Bidder Won Percentage: ' + str(value / total_simulation))
        if key == 4:
            logging.info('2nd Bidder Won Percentage: ' + str(value / total_simulation))
        if key == 3:
            logging.info('3rd Bidder Won Percentage: ' + str(value / total_simulation))
        if key == 2:
            logging.info('4th Bidder Won Percentage: ' + str(value / total_simulation))
        if key == 1:
            logging.info('Lowest Bidder Won Percentage: ' + str(value / total_simulation))


def main():
    """
    Main Driver
    :return:
    """
    logging.getLogger().setLevel(logging.INFO)
    random.seed(time.time())

    start_budget = 500

    horse_field_len = 100
    dice_base = 20
    bidding_simulation_round = 10
    total_simulation = 100000

    dice_modifiers = [0, 0, 0, 0, 0]
    start_modifiers = [8, 5, 3, 1, 0]
    reward_multiplier = 2

    players = []
    dices = []

    winner_bid_rank_map = {}

    # Populate Dices/Horses and Players
    for i in range(5):
        dices.append(Dice(dice_base + dice_modifiers[i]))
        players.append(Player('Player ' + str(i), i + 1))
        # Init winner map
        winner_bid_rank_map[i + 1] = 0

    logging.info('Simulating...')

    for i in range(total_simulation):
        re_init_players(players)
        logging.debug('Simulation #' + str(i))
        winner_bid_rank_map[simulate_game(players, dices, horse_field_len,
                                          bidding_simulation_round, start_modifiers)] += 1

    log_stats(winner_bid_rank_map, total_simulation)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
