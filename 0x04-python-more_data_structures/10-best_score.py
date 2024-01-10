#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = next(iter(a_dictionary))
    for key in a_dictionary:
        if a_dictionary[key] >= a_dictionary[max_score]:
            max_score = key
    return max_score
