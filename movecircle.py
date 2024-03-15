from  graphics  import *
def  main():
    win = GraphWin(1000,1000)
    shape = Circle(Point (50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in  range (10):
        p = win.getMouse ()
        c = shape.getCenter ()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        print('previous center', c.getX(), c.getY())
        print('Current center ', p.getX(), p.getY())
        shape.move(dx , dy)
    win.close()
main()