#!/usr/bin/env python3

i = 0
for alpha in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alpha - i)), end="")
    i = 32 if i == 0 else 0
