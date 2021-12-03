from numpy import arange

# Where should the rules/win stats come from?
# from original import main
from modified import main

# How do you think players will bid?
# best case: [5, 4, 3, 2, 1]
# worse case: [2500, 4, 3, 2, 1]
bids = [2500, 4, 3, 2, 1]

# What range of multipliers are you interested in? (min, max, step)
possible_reward_multipliers = [i for i in arange(2, 5, .25)]


num_wins = main()
total_races = sum(num_wins)
win_probs = [w/total_races for w in num_wins]
total_pot = sum(bids)


print()
print("Reward Multiplier | Expected Profit")
print("------------------+----------------")
for mult in possible_reward_multipliers:
    expected_loss_components = [0 for i in range(5)]
    for i in range(5):
        expected_loss_components[i] = bids[i] * win_probs[i] * mult
    total_expected_loss = sum(expected_loss_components)
    net = total_pot - total_expected_loss

    print("{:^18.3F}|{:>16.2F}".format(mult, net))
