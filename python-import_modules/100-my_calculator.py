#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    arguments = len(sys.argv)
    if (arguments != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    match operator:
        case "+":
            result = add(a, b)
        case "-":
            result = sub(a, b)
        case "*":
            result = mul(a, b)
        case "/":
            result = div(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
