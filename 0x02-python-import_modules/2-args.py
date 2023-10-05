#!/usr/bin/python3
import sys
argv = sys.argv
argc = len(argv) - 1

if __name__ == "__main__":
    print("{} argument".format(argc), end="")
    if argc != 1:
        print("s", end="")
    print(".") if argc == 0 else print(":")

    if argc >= 1:
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
