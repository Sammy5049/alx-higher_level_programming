#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
     """Divides two lists element by element.

     Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.

    """
    my_list_3 = []

    for new in range(0, list_length):
        try:
            result = my_list_1[new] / my_list_2[new]
        except TypeError:
            print("Wrong Type")
            result = 0
        except ZeroDivisionError:
            print("Division by 0")
            result = 0
        except IndexError:
            print("Out of range")
            result = 0
        finally:
            my_list_3.append(result)
    return (my_list_3)
