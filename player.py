class Player:
    def __init__(self, name, bid_amount):
        self.bid_amount = bid_amount
        self.name = name

    def get_bid_amount(self):
        return self.bid_amount

    def increase_bid(self, value):
        self.bid_amount += value


