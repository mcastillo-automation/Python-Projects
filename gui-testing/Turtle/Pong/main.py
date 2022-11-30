from turtle import Screen
from time import sleep
from scoreboard import Scoreboard
from paddles import Paddle
from ball import Ball

# setup Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

# setup paddles/ball
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

# setup scoreboard
scoreboard = Scoreboard()

# setup listeners w/key inputs
screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

game_over = False

while game_over is False:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.increase_score_l()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.increase_score_r()
        ball.reset_position()
        sleep_value = 0.1

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        game_over = True

screen.exitonclick()
