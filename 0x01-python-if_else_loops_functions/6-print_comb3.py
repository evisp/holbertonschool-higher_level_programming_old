#!/usr/bin/python3
for d1 in range (10):
    for d2 in range (10):
        if d1 == 8 and d2 == 9:
            print("{}{}".format(d1, d2))
        elif d1 < d2:
            print("{}{}".format(d1, d2), end=", ")
