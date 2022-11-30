from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 80, "normal")
GAME_OVER = ("courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setpos(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.setpos(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        if self.l_score == 10:
            self.write("Player 1 Wins!", align=ALIGNMENT, font=GAME_OVER)
        else:
            self.write("Player 2 Wins!", align=ALIGNMENT, font=GAME_OVER)
