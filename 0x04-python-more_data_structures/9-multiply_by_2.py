#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multi_dic = {}
    for key, value in a_dictionary.items():
        multi_dic[key] = value * 2
    return multi_dic
