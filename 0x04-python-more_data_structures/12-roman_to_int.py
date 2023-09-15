#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    roman_numeral = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }

    result = 0

    value_prev = 0

    for num_key in roman_string[::-1]:
        value = roman_numeral[num_key]

        if value_prev > value:
            result -= value
        else:
            result += value
        value_prev = value
    return result
