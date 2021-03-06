#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    a matrix divided function: matrix_divided():
    >>> matrix_divided(m, 1)
    m
    """


def matrix_divided(matrix, div):
    """
    Arguments:
        matrix{[list of int or float]} -- [the matrix to be divided]

    Keyword Arguments:
        div {int or float} -- [the number to divide by]

    Raises:
        TypeError: [if matrix not list or its elements not int or float]
        TypeError: [if len of one of the items not quel to others]
        ZeroDivisionError: [if div == 0]

    Returns:
        [list] -- [division of list by div]
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(lists, list) for lists in matrix)):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integer/float")

    if not all(all(isinstance(i, (float, int))
                   for i in row) for row in matrix):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in row] for row in matrix]
