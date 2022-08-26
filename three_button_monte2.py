# three_button_monte2.py

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

    # Draw retry and quit buttons
    retryB = Button(win, Point(1 * win_width/3, 3 * win_height/4), win_width/7, win_height/7, "Retry")
    quitB = Button(win, Point(2 * win_width/3, 3 * win_height/4), win_width/7, win_height/7, "Quit")
    quitB.activate()

    wins = 0
    losses = 0

    win_display = Text(Point(1 * win_width/4, win_height/8), f"Wins: {wins:2>}")
    win_display.draw(win)
    loss_display = Text(Point(3 * win_width/4, win_height/8), f"Losses: {losses:2>}")
    loss_display.draw(win)
    
    # Game loop
    pt = win.getMouse()
    while not quitB.clicked(pt):
        # Randomly select winning button
        winner = random.randint(1, 3)
        # Determine result
        if b1.clicked(pt) and winner == 1:
            message.setText(f"You won! Door {winner} was the correct door. Try again?")
            b2.deactivate()
            b3.deactivate()
            wins += 1
            win_display.setText(f"Wins: {wins:2>}")
        elif b2.clicked(pt) and winner == 2:
            message.setText(f"You won! Door {winner} was the correct door. Try again?")
            b1.deactivate()
            b3.deactivate()
            wins += 1
            win_display.setText(f"Wins: {wins:2>}")
        elif b3.clicked(pt) and winner == 3:
            message.setText(f"You won! Door {winner} was the correct door. Try again?")
            b1.deactivate()
            b2.deactivate()
            wins += 1
            win_display.setText(f"Wins: {wins:2>}")
        else:
            message.setText(f"You lost! Door {winner} was the correct door. Try again?")
            b1.deactivate()
            b2.deactivate()
            b3.deactivate()
            losses += 1
            loss_display.setText(f"Losses: {losses:2>}")

        # Check for another round
        retryB.activate()
        pt = win.getMouse()
        if retryB.clicked(pt):
            message.setText("Click on the winning door!")
            b1.activate()
            b2.activate()
            b3.activate()
            retryB.deactivate()
            pt = win.getMouse()
        
    # Game loop over
    win.close()

main()
