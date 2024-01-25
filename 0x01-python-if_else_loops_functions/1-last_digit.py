#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
print("Last digit of {} is {}".format(number,number_string[-1]), end=' ')
number_int = int(number_string[-1])
if number_int > 5:
    print("and is greater than 5")
elif number_int == 0:
    print("and is 0")
elif number_int < 6:
    print("and is less than 6 and not 0")
        
