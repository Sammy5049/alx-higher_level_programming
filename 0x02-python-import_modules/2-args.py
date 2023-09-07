#!/usr/bin/python3


def main():
    import sys

    length = len(sys.argv)

    if length - 1 == 0:
        print("0 arguments.")
    elif length - 1 == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length - 1))
    for i in range(length - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))


if __name__ == "__main__":
    main()