import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create actors
timmy = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Keyboard actions
screen.listen()
screen.onkeypress(timmy.go_up, "Up")


# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Crante and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect crossing
    if timmy.crossed():
        timmy.start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
