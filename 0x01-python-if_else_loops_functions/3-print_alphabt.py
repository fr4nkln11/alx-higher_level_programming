#!/usr/bin/python3
ascii_char = 97
while ascii_char < 123:
    if ascii_char != 101 and ascii_char != 113:
        print("{}".format(chr(ascii_char)), end="")
    ascii_char += 1
