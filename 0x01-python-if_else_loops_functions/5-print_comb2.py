#!/usr/bin/python3
for nr in range(0, 100):
    if nr < 99:
        print("{:02}".format(nr), end=", ")
    else:
        print("{}".format(nr))
