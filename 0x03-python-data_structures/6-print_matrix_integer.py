#!/usr/bin/python3

"""Here row -> Is the row of the matrix
   Here val -> is the value in the current row
"""


def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for val in range(len(matrix[row])):
            print("{:d}".format(matrix[row][val]), end=" ")
        print()
