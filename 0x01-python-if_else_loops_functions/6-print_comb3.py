#!/usr/bin/python3

for tens_digit in range(9):
    for units_digit in range(tens_digit + 1, 10):
        separator = ", " if tens_digit < 8 else "\n"
        print("{:d}{:d}".format(tens_digit, units_digit), end=separator)
