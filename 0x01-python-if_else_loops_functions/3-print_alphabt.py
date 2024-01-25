#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if 'q' in chr(i) or 'e' in chr(i):
        continue
    print("{}".format(chr(i)), end='')
