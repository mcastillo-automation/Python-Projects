from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def shift_clockwise():
    turtle.setheading(turtle.heading() + 10)


def shift_counterclockwise():
    turtle.setheading(turtle.heading() - 10)


def clear():
    turtle.reset()


screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(shift_clockwise, "a")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(shift_counterclockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
