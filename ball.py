from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(20)
        self.speed(5)

    def moving(self):
        self.forward(20)

    def rebound(self):
        if 0 <= self.heading() <= 90:
            self.setheading(self.heading()+90)
        elif self.heading() <= 180:
            self.setheading(self.heading()+90)
        elif self.heading() <= 270:
            self.setheading(self.heading()+90)
        elif self.heading() > 270:
            self.setheading(self.heading() - 270)

