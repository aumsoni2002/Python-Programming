import turtle
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
for _ in range(72):
    t.pencolor(random_color())
    t.circle(100)
    t.left(5)

s = turtle.Screen()
s.exitonclick()