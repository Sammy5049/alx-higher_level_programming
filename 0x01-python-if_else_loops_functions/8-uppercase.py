#!/usr/bin/python3
def uppercase(str):
    letter = str
    for chara in range(len(str)):
        check = ord(letter[chara])
        if check >= 97 and check <= 122:
            dig = check - 32
        else:
            dig = check
        newCha = chr(dig)
        if chara == len(str) - 1:
            print("{}".format(newCha))
        else:
            print("{}".format(newCha), end='')
