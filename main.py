import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

#create starting screen and objects
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
player = Player()
premenant = Scoreboard()
welcome= Scoreboard()
premenant.draw_screen()
level_writer = Scoreboard()
level_writer.level()
supress = 0

#controls
screen.listen()
screen.onkeypress(key = "Up", fun=player.move)
screen.onkeypress(key = "Down", fun=player.down)
game_start =0
game_is_on = True
welcome.welcome_msg()
premenant.high_score()

while game_is_on:
    time.sleep(0.05)
    if supress >= 6:
        car.create_car()
        supress = 0
        if level_writer.Level > 1:
            supress+=level_writer.Level

    screen.update()


    game_start+=1
    if game_start <20:
        level_writer.goto(0, -50)
        level_writer.write("3", align='center', font=("Courier", 25, "normal"))
    if game_start == 20:
        level_writer.clear()
        level_writer.level()
    if game_start <40 and game_start>20:
        level_writer.goto(0, -50)
        level_writer.write("2", align='center', font=("Courier", 25, "normal"))
    if game_start == 40:
        level_writer.clear()
        level_writer.level()
    if game_start <60 and game_start>40:
        level_writer.goto(0, -50)
        level_writer.write("1", align='center', font=("Courier", 25, "normal"))
    if game_start ==60:
        level_writer.clear()
        level_writer.level()
    if game_start <80 and game_start>60:
        level_writer.goto(0, -50)
        level_writer.write("Go!", align='center', font=("Courier", 25, "normal"))
    if game_start ==80:
        level_writer.clear()
        level_writer.level()
        welcome.clear()




    supress+=1

    car.move_car()
    #dectect cars
    for cars in car.all_cars:
        if player.distance(cars) <10:
            print('dead')
            level_writer.game_over()
            game_is_on =False

    if player.ycor()>280:
        level_writer.increase_level()
        level_writer.clear()
        level_writer.level()
        player.move_back()
        car.level_up()


screen.exitonclick()