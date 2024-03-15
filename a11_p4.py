# JTMS-14
# problem 11.4.py
# Abel Mengistu
# abmengistu@jacobs-university.de

class Vehicle(object): # Creates parent class vehicle
    def __init__(self,maxspeed, mileage):
        self._maxspeed = maxspeed
        self._mileage = mileage
    def __str__(self):
        return "Maximum speed = " + str(self._maxspeed) + \
                " and Mileage = " + str(self._mileage)


# Creates child class Bus and applies the parent class vehicle
class Bus(Vehicle):
    def __init__(self, maxspeed, mileage):
        Vehicle.__init__(self,maxspeed, mileage) # the vehicle class property is copied

#creating of objects

v1 = Vehicle(120, 45)
v2 = Vehicle(135, 65)
print("Vehicle 1:",v1)
print("Vehicle 2:",v2)

b1 = Bus(100, 76)
b2 = Bus(85, 56)
print("Buss 1:", b1)
print("Buss 2:",b2)

