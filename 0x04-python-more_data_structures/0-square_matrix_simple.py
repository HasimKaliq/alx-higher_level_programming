#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matix = [ [], [], [] ]
    idx = 0
    for i in matrix:
        for j in i:
           square = j * j
           new_matix[idx].append(square)
        idx += 1
    return new_matix
