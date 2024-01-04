#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
sum_1 = add(a, b)
diff = sub(a, b)
product = mul(a, b)
quoitent = div(a, b)

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, sum_1))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, product))
    print("{} / {} = {}".format(a, b, quoitent))
