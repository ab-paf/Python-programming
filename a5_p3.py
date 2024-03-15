# JTMS-14
# problem 5.3.py
# Abel Mengistu
# abmengistu@jacobs-university.de
import math

def volume_of_sphere(r):
    volume = 4/3*math.pi*r*r*r
    return volume
r = float(input("Enter radius of sphere: "))
result = volume_of_sphere(r)
print("The volume of sphere radius ", r, "is", result)