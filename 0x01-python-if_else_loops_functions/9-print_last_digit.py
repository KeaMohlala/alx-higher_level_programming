#!/usr/bin/python3
def print_last_digit(digit):
    if digit < 0:
        ldigit = digit % -(10)
        print(-(ldigit), end="")
    else:
        ldigit = digit % 10
        print(ldigit, end ="")
    return abs(ldigit)
