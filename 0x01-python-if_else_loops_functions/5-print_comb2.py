#!/usr/bin/python3
for i in range(99):
    if i < 98:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(99))

