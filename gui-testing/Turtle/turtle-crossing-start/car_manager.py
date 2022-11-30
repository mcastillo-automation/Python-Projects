import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.pu()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setpos(300, random.randint(-240, 240))
            self.car_list.append(new_car)

    def move(self):
        for cars in self.car_list:
            new_x = cars.xcor() - self.car_speed
            cars.setpos(new_x, cars.ycor())

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
