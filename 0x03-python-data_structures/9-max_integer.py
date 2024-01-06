#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    _max = my_list[0]
    for i in range(len(my_list)):
        is_max = my_list[i]
        if is_max >= _max:
            _max = is_max
    return _max
