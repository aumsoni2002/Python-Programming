from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x=x_cor, y=y_cor)
        self.setheading(90)

    def move_up(self):
        self.forward(50)

    def move_down(self):
        self.backward(50)