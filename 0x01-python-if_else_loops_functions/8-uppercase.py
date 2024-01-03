#!/usr/bin/python3
def uppercase(str):
    for index in str:
        if ord(index) >= 97 and ord(index) <= 122:
            index = chr(ord(index) - 32)
        print("{}".format(index), end="")
    print()
