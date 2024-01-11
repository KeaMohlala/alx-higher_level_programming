#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    if my_list is None:
        return
    seen = set()
    _sum = 0
    for i in my_list:
        if i not in seen:
            _sum += i
            seen.add(i)
    return _sum
