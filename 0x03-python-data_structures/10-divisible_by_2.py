#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    length = len(my_list)
    my_new_list = [None] * length

    for i in range(length):
        if my_list[i] % 2 == 0:
            my_new_list[i] = my_list[i]
    return my_new_list
