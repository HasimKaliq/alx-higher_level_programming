#!/usr/bin/python3

"""Here row -> Is the row of the matrix
   Here val -> is the value in the current row
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            continue
        else:
            for val in row:
                print("{:d}".format(val), end=" ")
            print()
