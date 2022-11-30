from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 15, "normal")
DATA = "./data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 280)
        self.score()

    def score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def read_high_score(self):
        try:
            with open(DATA) as file:
                return int(file.read())
        except IOError:
            with open(DATA, mode='w') as file:
                file.write("0")
            with open(DATA) as file:
                return int(file.read())

    def write_high_score(self):
        with open(DATA, mode='w') as file:
            file.write(f"{self.current_score}")

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.write_high_score()
        self.current_score = 0
        self.score()

    def increase_score(self):
        self.current_score += 1
        self.score()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
