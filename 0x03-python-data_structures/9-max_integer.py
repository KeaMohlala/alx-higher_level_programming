#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            is_max = my_list[i]
            if is_max >= _max:
                _max = is_max
        return _max
