#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
from sys import argv

argc = len(argv)
operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
        }

if __name__ == "__main__":
    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if operator not in operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, operators[operator](a, b)))
