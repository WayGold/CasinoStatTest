import random
from typing import List # mypy static typing

def d20() -> int:
    return random.randint(1, 20)

def player1() -> int:
    return d20() + 5

def player2() -> int:
    return d20() + 2

def player3() -> int:
    return d20()

def player4() -> int:
    return max(d20() - 1, 0)

def player5() -> int:
    return max(d20() - 2, 0)

def race_turn(pos: List[int]) -> None:
    pos[0] += player1()
    pos[1] += player2()
    pos[2] += player3()
    pos[3] += player4()
    pos[4] += player5()

def game() -> int:
    pos = [0 for i in range(5)]

    while( not any([p >= 50 for p in pos]) ):
        # game not over
        race_turn(pos)
    # game over

    # check for ties
    farthest = max(pos)
    count = pos.count(farthest)
    while (count > 1):
        race_turn(pos)
        farthest = max(pos)
        count = pos.count(farthest)
    # ties resolved

    # return winner
    winner = pos.index(farthest)
    return winner


def main():
    num_wins = [0 for i in range(5)]
    for i in range(100000):
        winner = game()
        num_wins[winner] += 1
    print(num_wins)



if __name__ == '__main__':
    main()