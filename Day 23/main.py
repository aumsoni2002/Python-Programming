import time
import itertools
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tim_the_turtle = Player()
screen.onkeypress(tim_the_turtle.move_forward, "Up")

random_cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
loop_tracker = itertools.count(start=1)
while game_is_on:
    current_iteration = next(loop_tracker)
    time.sleep(0.1)
    screen.update()

    if current_iteration % 6 == 0:
        random_cars.create_cars()
    random_cars.move_cars()

    # Detect collision with Cars
    for car in random_cars.cars:
        if car.distance(tim_the_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if turtle reaches the finish line
    if tim_the_turtle.is_at_finish_line():
        tim_the_turtle.back_to_start()
        scoreboard.increase_level()
        random_cars.increase_speed()

screen.exitonclick()
