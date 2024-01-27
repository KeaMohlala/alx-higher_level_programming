#!/usr/bin/python3
"""
This module has one function that divides
all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    function divides all elements of the matrix
    Each element is divided by div and rounded to two decimals
    A new matrix is returned

    Args:
    matrix: the list of lists
    div: the number to divide each matrix element by

    Raises:
    TypeError: If matrix is not a lists of lists,
    if all elements in the matrix are not integer or float,
    if rows of the matrix are not the same size
    if div is not an integer or float
    ZeroDivisionError: if div is equal to 0

    Return:
    new matrix with all elements divided by div
    rounded to two decimal places
    """
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix) != list or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(all(type(element) in [int, float] for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
