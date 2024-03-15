from graphics import *

def main():

    win = GraphWin("Simple interaction", 250,250)
    #Text(Point(70,50), "size side x ").draw(win)
    input = Entry(Point(80,50),5)
    input.setText("")
    input.draw(win)
    win.getMouse()

    s = eval(input.getText())
    print(s)
    square = Rectangle(Point(125 - s*2, 125 - s*2), Point(125 + s*2, 125 + s*2))
    square.setFill("red")
    square.setOutline("blue")
    square.draw(win)


    win.getMouse()
    win.close()

main()

"""import random
from random import randint
results = {6:0,5:0,4:0,3:0,2:0,1:0}
output = []

for i in range(100):
    roll = random.randint(1,6)
    results[roll]+= 1
    output.append(roll)

try:
    f = open("dieroll.dat", "w")
    for e in output:
        f.write(str(output))
    #f.write("{:<4} {:>9}".format("die", "roll"))
    f.write("\n")

    for i in results.keys():
        f.write("{:<4} {:>9}".format(i, results[i]))
        f.write("\n")
except FileExistsError:
    print("file not found")"""

"""start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
step = int(input("Enter the step value: "))

# Print the table header
print("{:>5s}{:>9s}{:>11s}".format("nr", "euro", "usd"))

# Iterate over the range of values and convert each value to USD
count = 1
for i in range(start, stop+1, step):

    print("{:>5.1f}{:>9.3f}{:>11.3f}".format(count, i , i*1.22))
    count+=1"""
