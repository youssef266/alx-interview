#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Prime Game
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(n):
        primes = get_primes(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = []
    for n in nums:
        winners.append(can_win(n))

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
