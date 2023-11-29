#!/usr/bin/python3
import random

# Generate a random integer between -10000 and 10000
number = random.randint(-10000, 10000)

# Calculate the last digit
if number < 0:
    last_num = number % -10
elif number >= 0:
    last_num = number % 10

# Check conditions based on the last digit
if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
