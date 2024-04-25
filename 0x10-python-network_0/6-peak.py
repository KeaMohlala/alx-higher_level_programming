#!/usr/bin/python3
"""
This module contains the find_peak function,
which finds a peak in a list of unsorted integers.
The function uses a binary search approach to find a peak element efficiently.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a binary search approach.

    Args:
    list_of_integers (list): A list of unsorted integers.

    Returns:
    int: The peak element if found, otherwise None.
    """
    start, end = 0, len(list_of_integers) - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_of_integers[mid] > list_of_integers[mid - 1]\
        and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start] if start < len(list_of_integers) else None
