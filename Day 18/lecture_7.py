import random
import turtle

t = turtle.Turtle()
t.shape("turtle")
turtle.colormode(255)

t.width(10)
directions = [0, 90, 180, 270]
t.speed(9)
for _ in range(100):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    t.pencolor((R, G, B))
    t.setheading(random.choice(directions))
    t.forward(25)


s = turtle.Screen()
s.exitonclick()