# JTMS-14
# problem 9.7.py
# Abel Mengistu
# abmengistu@jacobs-university.de

from article import *

n = int(input("Enter a number here: "))
count = 1
material = []
while n > count:
    x = input("Enter article: ")
    y = input("Enter article type: ")
    t = input("Enter article color: ")
    r = input("Enter article rating: ")
    f = input("Enter article price: ")

    count += 1
    material.append(Article(x, y, t, r, f))

for i in material:
    print(i)
