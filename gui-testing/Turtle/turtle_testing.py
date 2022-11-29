from turtle import Turtle, Screen, colormode
from random import choice, randint
from sys import exit

"""
Just testing turtle module for gui testing
"""

# Configure Turtle
turtle = Turtle()
turtle.speed("fastest")
colormode(255)


# Quick function to determine color of drawings.
def turtle_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


# Quick movement/turn test
def move_and_turn(n_times):
    for n in range(n_times):
        turtle.forward(100)
        turtle.right(90)


# Checking to see how to handle dashed lines.
def dashed_line(n_times):
    for n in range(n_times):
        turtle.forward(10)
        turtle.up()
        turtle.forward(10)
        turtle.down()


# Making simple code that takes a range of sides to create regular shapes.
def shape_master(start, stop, distance=100):
    if 3 <= start < stop:
        def shape(number_of_sides):
            def movement(angle):
                turtle.right(angle)
                turtle.forward(distance)

            for n in range(number_of_sides):
                movement(360 / number_of_sides)

        for x in range(start, stop + 1):
            turtle.color(turtle_color())
            shape(x)
    else:
        print("Please enter a valid number of sides.")
        exit()


# Attempting the random walk in Turtle
def rand_walk(n_iterations):
    turtle.width(15)
    angle = [0, 90, 180, 270]
    for x in range(n_iterations):
        turtle.color(turtle_color())
        turtle.forward(randint(10, 50))
        turtle.setheading(choice(angle))


# Making a spirograph.
def spirograph(radius, step):
    # Make a circle, change angle, then draw another circle
    angle = 0
    try:
        while abs(angle) <= 360:
            turtle.setheading(angle)
            turtle.color(turtle_color())
            turtle.circle(radius)
            if step != 0:
                angle += step
            else:
                print("Please enter a non-zero step.")
                exit()
    except TypeError:
        print("Please enter a valid integer.")
        exit()


# move_and_turn(4)
# dashed_line(10)
# shape_master(3, 10)spirograph(100, 10)
# rand_walk(200)

screen = Screen()
screen.exitonclick()
