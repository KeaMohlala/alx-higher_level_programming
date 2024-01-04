#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_count = (len(sys.argv)) - 1
    sum_1 = 0
    if arg_count == 0:
        print("0")
    else:
        for i in range(1, arg_count + 1):
            sum_1 += int(sys.argv[i])
        print("{}".format(sum_1))
