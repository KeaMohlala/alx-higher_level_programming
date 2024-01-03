#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ldigit = number % -(10)
        print(-(ldigit), end="")
    else:
        ldigit = number % 10
        print(ldigit, end="")
    return abs(ldigit)
