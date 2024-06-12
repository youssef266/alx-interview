#!/usr/bin/python3
"""
0-minoperations.py
Module that defines a function called minOperations that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    minOperations - calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    oper = 0
    min_oper = 2
    while n > 1:
        while n % min_oper == 0:
            oper += min_oper
            n /= min_oper
        min_oper += 1
    return oper
