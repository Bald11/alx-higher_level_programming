#!/usr/bin/python3
islower = __import__('7-islower').islower

def uppercase(str):
    str = str + '\n'
    for i in str:
        if islower(i):
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print(i, end='')
    return None

