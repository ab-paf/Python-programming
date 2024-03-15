# JTMS-14
# problem 11.2.py
# Abel Mengistu
# abmengistu@jacobs-university.de


# asking for integer
s = input("Enter a string: ")
n = int(input("Enter an integer: "))

# using try and except for type error

try:
    print(s + n)
except TypeError as err:
    print("Error: ", err)


# using try and except for value error

import math

square = int(input("Enter a number: "))
try:
    math.sqrt(square)
except ValueError as vlurr:
    print('Positive number expected for square root operation', vlurr)


# using try and except for import error

func = input("Enter function to import: ")
try:
    from crypt import func
except ImportError as ie:
    print("It cannot import module and submodule", ie)