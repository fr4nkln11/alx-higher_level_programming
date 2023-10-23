#!/usr/bin/python3
def safe_print_division(a: int, b: int) -> float | None:
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("{}".format(result))
        return result
