# three_button_monte.py

from graphics import *
from button import *
import random

def main():
    # Draw window
    win_width = 500
    win_height = 500
    win = GraphWin("Three Button Monte", win_width, win_height)

    # Present instruction message
    message = Text(Point(win_width/2, win_height/5), "Click on the winning door!")
    message.draw(win)
    
    # Draw the three buttons
    b1 = Button(win, Point(1 * win_width/4, win_height/2), win_width/5, win_height/5, "Door 1")
    b1.activate()
    b2 = Button(win, Point(2 * win_width/4, win_height/2), win_width/5, win_height/5, "Door 2")
    b2.activate()
    b3 = Button(win, Point(3 * win_width/4, win_height/2), win_width/5, win_height/5, "Door 3")
    b3.activate()
    
    # Randomly select winning button
    winner = random.randint(1, 3)

    # Get user's door selection
    pt = win.getMouse()

    # Determine result
    if b1.clicked(pt) and winner == 1:
        message.setText(f"You won! Door {winner} was the correct door.")
        b2.deactivate()
        b3.deactivate()
    elif b2.clicked(pt) and winner == 2:
        message.setText(f"You won! Door {winner} was the correct door.")
        b1.deactivate()
        b3.deactivate()
    elif b3.clicked(pt) and winner == 3:
        message.setText(f"You won! Door {winner} was the correct door.")
        b1.deactivate()
        b2.deactivate()
    else:
        message.setText(f"You lost! Door {winner} was the correct door.")
        b1.deactivate()
        b2.deactivate()
        b3.deactivate()

if __name__ == "__main__":
    main()
