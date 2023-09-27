#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Result is: {}".format(result))

    return (result)
