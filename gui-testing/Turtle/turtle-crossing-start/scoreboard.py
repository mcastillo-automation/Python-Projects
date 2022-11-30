from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level_num = 0
        self.hideturtle()
        self.pu()
        self.setpos(-280, 240)
        self.current_lvl()

    def current_lvl(self):
        self.write(f"Level: {self.level_num}", align="left", font=FONT)

    def update_lvl(self):
        self.clear()
        self.level_num += 1
        self.current_lvl()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
