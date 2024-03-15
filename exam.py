"""
class Tourist(object):

    def __init__(self, first, last, countries):
        self._first= first
        self._last = last
        self._countries = countries


    def __str__(self):
        return "First name: " + self._first + "\nlast name: " + self._last + "\ncountries: " + str(self._countries)






f = Tourist("Abel","Mengistu", ["Canada", "america", "ethiopia"])

print(f)
"""

"""class Tourist(object):
    def _init_(self, fname, lname, countries):
        self._fname = fname
        self._lname = lname
        self._countries = countries

    def getfname(self):
        return self._fname

    def setfname(self, newname):
        self._fname = newname

    def _eq_(self, other):
        if len(self._countries) == len(other._countries):
            return True
        else:
            return False

    def _lt_(self, other):
        if len(self._countries) < len(other._countries):
            return True
        else:
            return False

    def _gt_(self, other):
        if len(self._countries) > len(other._countries):
            return True
        else:
            return False

    def _str_(self):
        return "firstname = " + self._fname + "\nlastname = " + self._lname + "\ncountries = " + str(self._countries)"""


""""# Read values from the user
x = int(input("Enter an integer value for x: "))
y = input("Enter a single character for y: ")
z = float(input("Enter a float value for z: "))

# Calculate the ASCII code for character y
asciiCode = ord(y)

# Calculate the product of x, the ASCII code of y, and z
product = x * asciiCode * z

# Print the result
print("The product of x, the ASCII code of y, and z is:", product)"""

"""list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d", "e", "f"]

# Initialize the resulting list
list3 = []

# Concatenate the two input lists
for i in range(len(list2)):
    if i < len(list1):
        list3.append(str(list1[i]) + list2[i])
    else:
        list3.append(list2[i])

# Print the resulting list
print(list3)
"""

# Read the start, stop, and step values from the user
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
step = int(input("Enter the step value: "))

# Print the table header
print("{:>5s}{:>9s}{:>11s}".format("nr", "euro", "usd"))

# Iterate over the range of values and convert each value to USD
count = 1
for i in range(start, stop+1, step):

    print("{:>5.1f}{:>9.3f}{:>11.3f}".format(count, i , i*1.22))
    count+=1

"""names = []

def pop(queue, name):
    if len(queue) == 0:
        return None
    else:
        queue.remove(name)

def is_empty(queue):
    return len(queue) == 0

# Test the functions
names.append("Alice")
names.append("Bob")
names.append("Charlie")
print(pop(names, "Alice"))  # should print None
print(pop(names, "Bob"))  # should print None
print(is_empty(names))  # should print False
print(pop(names, "Charlie"))  # should print None
print(is_empty(names))  # should print True"""

"""import random
import sys

# Roll the die 100 times and write the results to a file
try:
    with open("dieroll.dat", "w") as f:
        for i in range(100):
            roll = random.randint(1, 6)
            f.write(str(roll) + "\n")

    # Calculate overall statistics and write them to the file
    with open("dierol.dat", "a") as f:
        f.write("\n")
        f.write("Overall statistics:\n")
        for i in range(1, 7):
            f.write(f"{i}: {roll.count(i)}\n")
except IOError:
    print("An error occurred while trying to open or write to the file.")
    sys.exit(1)"""

"""from graphics import *

# Create the window
win = GraphWin("Simple interaction", 250, 250)

# Read the size of the triangle from the user
size = int(Entry(Point(125, 125), 5).getText())

# Calculate the coordinates of the triangle's vertices
point1 = Point(125, 125)
point2 = Point(125 + size, 125)
point3 = Point(125, 125 - size)

# Draw the triangle
triangle = Polygon(point1, point2, point3)
triangle.setFill("green")
triangle.draw(win)

# Wait for the user to click in the window
win.getMouse()

# Close the window
win.close()"""

"""import csv

# Open the input and output CSV files
     inputFile = open("input.csv", "r") 
     outputFile = open("output.csv", "w", newline="")
    # Create CSV readers and writers
    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile)

    # Write the header row to the output file
    writer.writerow(["Name", "Major", "GPA"])

    # Iterate over the rows in the input file
    for row in reader:
        name, major, gpa = row
        if major == "IEM" and float(gpa) < 2.5:
            writer.writerow(row)"""


"""celsius = int(input("Enter degree: "))

if celsius < 0:
    print("It is very cold")
elif celsius <= 10:
    print("It is cold")
elif celsius > 10 and celsius < 20:
    print("It is warm")
else:
    print("It is hot")"""


import random
import sys

try:
    with open("dieroll.dat", "w") as file:
        for i in range(100):
            roll = random.randint(1, 6)
            file.write(f"Roll {i+1}: {roll}\n")

    with open("dieroll.dat", "r") as file:
        data = file.read()

    # Count the number of times each number was rolled
    counts = [data.count(str(i)) for i in range(1, 7)]

    # Write the overall statistics to the file
    with open("dieroll.dat", "a") as file:
        file.write("\nOverall statistics:\n")
        for i in range(1, 7):
            file.write(f"{i}: {counts[i-1]} times\n")
except:
    print("Failed to open dieroll.dat for writing")
    sys.exit()




queue = []

def add(queue, name):
  # Add the name at the end of the queue
  queue.append(name)

def is_empty(queue):
  # Return True if the queue is empty, False otherwise
  return len(queue) == 0

while True:
  com = input(" Command: ")
  if com == "a":
    name = input("Name: ")
    add(queue, name)
  elif com == "e":
    print(is_empty(queue))
  elif com == "p":
    print(queue)
  elif com == "q":
    break
