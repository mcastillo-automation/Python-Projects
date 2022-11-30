"""
Simple turtle racing game.
"""

import sys
from turtle import Turtle, Screen
from random import randint

SHAPE = "turtle"
green = Turtle(SHAPE)
purple = Turtle(SHAPE)
red = Turtle(SHAPE)
blue = Turtle(SHAPE)

turtles = [green, purple, red, blue]
colors = ["green", "purple", "red", "blue"]

# Setup Screen
screen = Screen()

# Config turtles and move to left of screen
X_COORD = -450
Y_COORD = -100
COLOR_INDEX = 0
for turtle in turtles:
    turtle.color(colors[COLOR_INDEX])
    COLOR_INDEX += 1
    turtle.pu()
    turtle.setpos(X_COORD, Y_COORD)
    Y_COORD += 50

while True:
    try:
        guess = screen.textinput("Guess!", "Which turtle will win?").strip().lower()
        if guess not in colors:
            print("Please enter a valid guess!")
        else:
            break
    except AttributeError:
        sys.exit()

GAME_OVER = False
FINISH_LINE = 450.00
WINNER = None


def move(color):
    """
    Just need a randint for determining how far ea. turtle moves.
    """
    color.forward(randint(10, 50))


while GAME_OVER is False:
    move(green)
    if green.xcor() >= FINISH_LINE:
        WINNER = "green"
        GAME_OVER = True
    move(purple)
    if purple.xcor() >= FINISH_LINE:
        WINNER = "purple"
        GAME_OVER = True
    move(red)
    if red.xcor() >= FINISH_LINE:
        WINNER = "red"
        GAME_OVER = True
    move(blue)
    if blue.xcor() >= FINISH_LINE:
        WINNER = "blue"
        GAME_OVER = True

if guess == WINNER:
    print("Congrats, you are the winner!")
else:
    print(f"{WINNER.capitalize()} won! Better luck next time!")

screen.exitonclick()
