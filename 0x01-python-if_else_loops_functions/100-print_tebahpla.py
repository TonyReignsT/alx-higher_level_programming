#!/usr/bin/python3

for char in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(char if char % 2 == 0 else char - ord('a') + ord('A'))), end="")
print()
