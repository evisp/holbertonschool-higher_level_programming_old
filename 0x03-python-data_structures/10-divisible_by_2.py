#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_list = [True if value % 2 == 0 else False for value in my_list]
    return bool_list
