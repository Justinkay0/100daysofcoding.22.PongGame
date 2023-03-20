import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def up(self):
        if self.heading() != 90:
            self.setheading(90)
        self.goto(y=self.ycor()+20, x=self.xcor())

    def down(self):
        if self.heading() != 270:
            self.setheading(270)
        self.goto(y=self.ycor()-20, x=self.xcor())

