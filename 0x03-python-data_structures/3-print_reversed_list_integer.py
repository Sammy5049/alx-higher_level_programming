#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    for list in my_list:
        print("{:d}".format(list))
