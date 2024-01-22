#!/usr/bin/python3
def safe_print_integer(value):
    if isinstance(value, str):
        if not value.replace(" ", "").isdigit():
            return False
    try:
        print("{:d}".format(int(value)))
    except ValueError:
        return False
    return True
