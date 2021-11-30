import random
import time


class Dice:
    def __init__(self, d_num):
        self.d_num = d_num

    def rand_roll(self):
        random.seed(time.time())
        return random.randint(1, self.d_num)
