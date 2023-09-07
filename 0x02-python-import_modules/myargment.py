# #!/usr/bin/python3
# import argparse
# import sys
# i = 0
# length = len(sys.argv)

# if length == 1:
#     print("{} arguments.".format(i))
# i = 1
# if length == 2:
#     print("{} argument:".format(i))
#     print("{}: {}".format(i, sys.argv[i]))

# if length > 2:
#     print("{} arguments:".format(length - 1))
#     for i in range(length):
#         if i != 0:
#             print("{}: {}".format(i, sys.argv[i]))


#!/usr/bin/python3
import argparse


def float_or_str(arg):
    try:
        return float(arg)
    except ValueError:
        return arg


def main():
    parser = argparse.ArgumentParser(description="A program to list args")
    parser.add_argument("argument", type=float_or_str,
                        nargs="*", help="List of arguments")

    myArgs = parser.parse_args()

    argLen = len(myArgs.argument)
    if myArgs.argument and argLen > 1:
        print("{}: arguments".format(argLen))
        for argME in range(argLen):
            print("{}: {}".format(argME, myArgs.argument[argME]))

    elif myArgs.argument and argLen == 1:
        print("{}: argument".format(argLen))
        for argME in range(argLen):
            print("{}: {}".format(argME, myArgs.argument[argME]))

    else:
        print("{} arguments.".format(argLen))


if __name__ == "__main__":
    main()
