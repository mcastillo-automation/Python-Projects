from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.pu()
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setpos(self.xcor(), new_y)

    def is_at_finish_line(self):
        return bool(self.ycor() >= FINISH_LINE_Y)

    def reset_game(self):
        self.setpos(STARTING_POSITION)
