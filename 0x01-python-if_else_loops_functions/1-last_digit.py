#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
if number < 0:
    last_digit = "-" + number_string[-1]
else:
    last_digit = number_string[-1]
print("Last digit of {} is {}".format(number,last_digit), end=' ')
number_int = int(last_digit)
if number_int > 5:
    print("and is greater than 5")
elif number_int == 0:
    print("and is 0")
elif number_int < 6:
    print("and is less than 6 and not 0")
