#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for j in my_list:
            if counter < x:
                print("{}".format(j), end="")
                counter += 1
        print()
        return (counter)
    except Exception as e:
        print("An error occured: {}".format(e))
        return (0)
