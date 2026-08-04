import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

y_pos = -100
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_pos)
    y_pos = y_pos + 30
    all_turtles.append(new_turtle)

print(all_turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for each_turtle in all_turtles:
        if each_turtle.xcor() > 230:
            winning_color = each_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")

            is_race_on = False

        rand_distance = random.randint(0, 10)
        each_turtle.forward(rand_distance)

screen.exitonclick()
