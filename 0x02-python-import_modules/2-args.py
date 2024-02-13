#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    output = ''
    if (len(sys.argv) == 1):
        output += '0 arguments.\n'
    elif (len(sys.argv) > 1):
        if (len(sys.argv) == 2):
            output += '1 argument:\n1: {}\n'.format(sys.argv[1])
        else:
            output += '{} arguments:\n'.format(len(sys.argv) - 1)
            for i in range(1, len(sys.argv)):
                output += '{}: {}\n'.format(i, sys.argv[i])
    print(output, end='')
