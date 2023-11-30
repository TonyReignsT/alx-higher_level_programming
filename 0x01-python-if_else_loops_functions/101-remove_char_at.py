#!/usr/bin/python3
def remove_char_at(my_str, n):
    if 0 <= n < len(my_str):
        result = ""
        for i in range(len(my_str)):
            if i != n:
                result += my_str[i]
        return result
    else:
        return my_str
