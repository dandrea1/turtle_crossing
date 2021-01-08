import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')
screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')

game_is_on = True
counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    counter += 1

    if counter % 6 == 0:
        car_manager.generate_car()

    # Detect Collision with Cars
    for car in car_manager.cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
