from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def moving(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def rebound(self):
        if 0 <= self.heading() <= 90:
            self.setheading(self.heading()+90)
        elif self.heading() <= 180:
            self.setheading(self.heading()+90)
        elif self.heading() <= 270:
            self.setheading(self.heading()+90)
        elif self.heading() > 270:
            self.setheading(self.heading() - 270)

