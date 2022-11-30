import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move_up, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.is_at_finish_line():
        player.reset_game()
        scoreboard.update_lvl()
        car_manager.speed_up()

    for cars in car_manager.car_list:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()