#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of the character is within the lowercase range
    return ord('a') <= ord(c) <= ord('z') if 'a' <= c <= 'z' else False

# Test the function
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('1'))  # False
