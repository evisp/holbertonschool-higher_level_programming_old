#!/usr/bin/python3

def no_c(my_string):
    no_c_string = ""
    for letter in my_string:
        if letter not in "cC":
            no_c_string += letter
    return no_c_string
