#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_val = [key for key, valued in a_dictionary.items() if valued == value]

    for key in delete_val:
        del a_dictionary[key]
    return a_dictionary
