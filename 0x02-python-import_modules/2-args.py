#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    nr_args = len(argv) - 1

    if nr_args == 0:
        print("0 arguments.")
    elif nr_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nr_args))

    for arg in range(nr_args):
        print("{}: {}".format(arg + 1, argv[arg + 1]))
