#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_new_square = Square(86)
    print(my_new_square.size)
    my_new_square.size = "88"
    print(my_new_square.size)
except Exception as e:
    print(e)
