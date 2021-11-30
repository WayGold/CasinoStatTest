# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dice import *
from player import *


def simulate_once(players, field_length):
    pass


def main():
    horse_field_len = 50
    largest_dice_num = 20
    dice_decrement = 2

    players = []
    dices = []

    # Populate Dices/Horses
    for i in range(5):
        dices.append(Dice(largest_dice_num - i * dice_decrement))

    # Assign Each Player their Dice/Horse
    for i, j in enumerate(dices):
        players.append(Player('Player ' + str(i), i, j))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
