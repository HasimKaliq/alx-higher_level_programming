#!/usr/bin/python3

"""Here row -> Is the row of the matrix
   Here val -> is the value in the current row
   This exist because "there's more than one way to solve a problem, find the most efficient
   But the most efficient might not be the most accurate
"""


def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for val in range(len(matrix[row])):
            print("{:d}".format(matrix[row][val]), end=" ")
        print()
