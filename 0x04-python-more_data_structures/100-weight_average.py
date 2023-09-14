#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0.0
    total_weight = 0.0
    mul = 0.0
    for num in my_list:
        score, weight = num
        total_weight += weight
        mul += score * weight
    if total_weight == 0:
        return 0.0
    average_wg = (mul / total_weight)
    return average_wg
