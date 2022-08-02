from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = -2.5
MOVE_INCREMENT = -10


class CarManager():
    def __init__(self):
        self.all_cars=[]
    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(0.75, 1.75)
        new_car.penup()
        color = COLORS[random.randint(0, 5)]
        new_car.color(color)
        y = random.randint(-200, 200)
        new_car.goto(300, y)
        self.all_cars.append(new_car)

    def move_car(self):
         for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE)


    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE -=2.5