import random
import turtle
from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
turtle.colormode(255)
for i in range(3, 11):
    turn_degree = 360 / i
    R = random.randint(0 , 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    t.pencolor((R, G, B))

    for j in range(0, i):
        t.forward(100)
        t.right(turn_degree)

s = Screen()
s.exitonclick()