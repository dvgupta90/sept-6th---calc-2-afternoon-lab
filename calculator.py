"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    input_string = "add num1 num2"
    tokens = input_string.split(" ")
    if token[0] == "q":
        break
    else:
        add(num1,num2)    