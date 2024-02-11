#!/usr/bin/python3
<<<<<<< HEAD
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i,j), end='\n')
        else:
            print("{}{}".format(i,j), end=', ')
=======
for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", " if j < 9 else "\n", flush=True)
>>>>>>> 8a8af720034fd0616efbbb2df4c6c7100da67488
