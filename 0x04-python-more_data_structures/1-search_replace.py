#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_new_list = []
    for i in my_list:
        if i == search:
            my_new_list.append(replace)
        else:
            my_new_list.append(i)
    return (my_new_list)
