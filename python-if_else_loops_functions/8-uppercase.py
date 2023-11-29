#!/usr/bin/python3
def uppercase(string):
    for i in range(len(string)):
        s = ord(string[i])
        if s >= 97 and s <= 122:
            s = s - 32
        print("{}".format(chr(s)), end="")
    print()
