"""
Contains the Snake class and associated constants.
"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Handles setup and actions for the snake in a Snake game
    """

    def __init__(self):
        # Instantiate Turtles
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        """
        Creates the snake. Is instantiated at class call.
        """
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        self.segment_list.append(segment)
        segment.pu()
        segment.setpos(position)

    def reset_game(self):
        for seg in self.segment_list:
            seg.goto(1000, 1000)
        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        """w
        Should be used in a while loop. Allows snake to move constantly/organically.
        """
        for segment_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[segment_num - 1].xcor()
            new_y = self.segment_list[segment_num - 1].ycor()
            self.segment_list[segment_num].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        """
        Re-orients the snake to face up.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        """
        Re-orients the snake to face down.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        """
        Re-orients the snake to face left.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        """
        Re-orients the snake to face right.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
