# JTMS-14
# problem 9.4.py
# Abel Mengistu
# abmengistu@jacobs-university.de

from rational import *

a = int(input("enter a numerator for 1st num: "))
b = int(input("enter a denominator of 1st num: "))
c = int(input("enter a numerator for 2nd num: "))
d = int(input("enter a denominator for 2nd num: "))

x = Rational(a, b)
y = Rational(c, d)

print(x.numerator())
print(x.denominator())
print(y.numerator())
print(y.denominator())

print(x.__add__(y))