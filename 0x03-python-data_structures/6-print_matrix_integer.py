#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        print(" ".join("{}".format(element) for element in line))
