#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numbers = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [0]
    print("{}".format(sum(numbers)))
