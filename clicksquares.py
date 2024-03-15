# JTMS-14
# problem 12.1.py
# Abel Mengistu
# abmengistu@jacobs-university.de
from graphics import *

def main():
    win = GraphWin()
    # creating a square using Rectangle class
    square = Rectangle(Point(10, 10), Point(40, 40))
    square.setOutline("red")
    square.setFill("red")
    square.draw(win) # drawing the square
    for i in range(10):
        p = win.getMouse()
        c = square.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        n_square = square.clone() # cloning the square
        n_square.move(dx, dy) # moving to new coordinates
        n_square.draw(win)
    win.close()

main()