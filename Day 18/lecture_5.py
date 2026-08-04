from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("red")

for _ in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


s = Screen()
s.exitonclick()