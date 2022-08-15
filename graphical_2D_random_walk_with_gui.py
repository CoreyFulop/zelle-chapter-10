# graphical_2D_random_walk_with_gui.py

from graphics import *
from button import *
import random
import math

def main():

    # Create window
    win_width = 500
    win_height = 500

    sidebar_width = 100

    win = GraphWin("Random Walk", win_width, win_height)

    llx = - (win_width/2 + sidebar_width)
    lly = - (win_height/2)
    urx = win_width/2
    ury = win_height/2

    win.setCoords(llx, lly, urx, ury)

    partition = Line(Point(llx + sidebar_width,lly), Point(llx + sidebar_width,ury))
    partition.draw(win) 

    # Create entry field for number of steps
    n = Entry(Point(llx + sidebar_width/2, ury - 100), 5)
    n.setText("Steps")
    n.draw(win)

    # Create buttons
    start = Button(win, Point(llx + sidebar_width/2, ury - 200), 50, 25, "Start")
    start.activate()
    quitbutton = Button(win, Point(llx + sidebar_width/2, ury - 300), 50, 25, "Quit")
    quitbutton.activate()

    # Event loop
    pt = win.getMouse()
    while not quitbutton.clicked(pt):
        if start.clicked(pt):
            steps = eval(n.getText())
            x = y = 0.0
            for i in range(steps):
                angle = random.random() * 2 * math.pi
                new_x = x + math.cos(angle)
                new_y = y + math.sin(angle)
                line = Line(Point(x, y), Point(new_x, new_y))
                line.setWidth(1)
                line.draw(win)
                x, y = new_x, new_y
        n.setText("Steps")
        pt = win.getMouse()
        
    # Shut up shop
    win.close()

main()
