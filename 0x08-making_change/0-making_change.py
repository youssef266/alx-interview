#!/usr/bin/python
"""
Making Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed for each total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins needed for each total
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return the minimum number of coins needed for the total
    return min_coins[total] if min_coins[total] != float('inf') else -1
