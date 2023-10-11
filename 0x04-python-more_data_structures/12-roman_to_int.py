#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or not isinstance(roman_string, str):
        return 0

    key_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            }

    ints = [key_numerals[x] for x in roman_string]

    for i in range(len(ints) - 1):
        if ints[i] < ints[i + 1]:
            ints[i] = -ints[i]

    return sum(ints)
