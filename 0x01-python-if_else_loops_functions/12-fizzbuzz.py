#!/usr/bin/python3

def fizz(fizz):
    return fizz % 3 == 0

def buzz(buzz):
    return buzz % 5 == 0

for i in range(1,101):
    if fizz(i) and buzz(i):
        print("FizzBuzz", end=' ')
    elif fizz(i):
        print("Fizz", end=' ')
    elif buzz(i):
        print("Buzz", end=' ')
    else:
        print(i, end=' ')
