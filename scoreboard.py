from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.left_score = 0
        self.right_score = 0
        self.setpos(x=0,y=250)

    def increase_score_left(self):
        self.left_score += 1

    def increase_score_right(self):
        self.right_score += 1

    def update_score(self):
        self.clear()
        self.write(arg=f'{self.left_score}     {self.right_score}', align='center', font=('Courier Regular', 24) )