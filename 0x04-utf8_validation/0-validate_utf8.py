#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    # Number of bytes in the current character
    num_bytes = 0

    # Iterate through each integer in the data set
    for num in data:
        # Check if the current integer is a continuation byte
        if num >> 6 == 0b10:
            # If it's not a valid continuation byte, return False
            if num_bytes == 0:
                return False
            # Decrement the number of bytes remaining for the current character
            num_bytes -= 1
        else:
            # Check the number of bytes required for the current character
            if num_bytes != 0:
                return False
            if num >> 7 == 0b0:
                num_bytes = 0
            elif num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False

    # If there are remaining bytes for the current character, return False
    if num_bytes != 0:
        return False

    # All checks passed, return True
    return True
