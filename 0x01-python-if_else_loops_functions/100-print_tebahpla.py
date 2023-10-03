#!/usr/bin/python3
case_flag = False
ascii_code = 122
character = chr(ascii_code)

while ascii_code > 96:
    if case_flag:
        character = chr((ascii_code - 97) + 65)
    else:
        character = chr(ascii_code)
    print("{}".format(character), end='')
    ascii_code -= 1
    case_flag = not case_flag
