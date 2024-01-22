#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    list_size = sum(1 for _ in my_list)
    try:
        for i in range(min(x, list_size)):
            print("{}".format(my_list[i]), end="")
            printed += 1
        print()
    except IndexError:
        for i in range(list_size):
            print("{}".format(my_list[i]), end="")
            printed += 1
        print()
    return printed
