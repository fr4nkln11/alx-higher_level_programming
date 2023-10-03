#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_code = ord(char)
        upper_char = char
        if (ascii_code > 96 and ascii_code < 123): # chech if is lower
            upper_char = chr((ascii_code - 97) + 65)
        print("{}".format(upper_char), end="")
    print("")
