#!/usr/bin/python3
import sys


def main():

    arguments = len(sys.argv)

    if (arguments == 1):
        print("0 arguments.")
    elif (arguments == 2):
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arguments - 1))
        for i in range(1, arguments):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
