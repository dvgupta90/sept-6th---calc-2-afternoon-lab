"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    input_string = input(">")
    token = input_string.split(" ")
    if token[0] == "q":
        break
    else:
        print (add(int(token[1]), int(token[2])))

        
