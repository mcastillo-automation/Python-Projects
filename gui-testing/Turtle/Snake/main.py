""""
A simple snake game built with Turtle
"""

from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setup/Config Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_right, "d")

game_over = False

while game_over is False:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
