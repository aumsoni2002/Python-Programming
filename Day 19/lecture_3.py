from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_drawing():
    tim.reset()

screen.listen()

screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=move_counter_clockwise, key="a")
screen.onkeypress(fun=move_clockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")

screen.exitonclick()
