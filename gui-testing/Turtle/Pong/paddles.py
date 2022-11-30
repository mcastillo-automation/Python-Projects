from turtle import Turtle

# STARTING_POSITIONS = [(-350, 0), (350, 0)]
MOVE_DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.setpos(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setpos(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.setpos(self.xcor(), new_y)
