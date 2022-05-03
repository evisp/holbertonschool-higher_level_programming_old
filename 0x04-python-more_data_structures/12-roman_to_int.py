#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    translate = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    num = 0
    while i < len(roman_string):
        if i+1<len(roman_string) and roman_string[i:i+2] in translate:
            num += translate[roman_string[i:i+2]]
            i = i + 2
        else:
            num += translate[roman_string[i]]
            i = i + 1
    return num
