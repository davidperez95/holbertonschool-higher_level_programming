#!/usr/bin/python3
import sys


def main():

    arguments = len(sys.argv)
    result = 0
    if (arguments == 1):
        print("0")
    else:
        for i in range(1, arguments):
            result += int(sys.argv[i])
        print("{:d}".format(result))


if __name__ == "__main__":
    main()
