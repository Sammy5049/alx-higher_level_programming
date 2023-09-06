#!/usr/bin/python3

def fizzbuzz():
    for numb in range(1, 101):
        if numb % 3 == 0:
            print("fizz", end=" ")
        elif numb % 5 == 0:
            print("buzz", end=" ")
        elif numb % 3 == 0 and numb % 5 == 0:
            print("fizzbuzz", end=" ")

        else:
            print(numb, end=" ")
