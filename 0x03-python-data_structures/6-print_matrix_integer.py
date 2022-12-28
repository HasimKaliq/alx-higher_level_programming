#!/usr/bin/python3

"""Here row -> Is the row of the matrix
   Here val -> is the value in the current row
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row:
            print("{:d}".format(val), end="")
            if val != row[-1]:
                print(' ', end='')
        print("")
