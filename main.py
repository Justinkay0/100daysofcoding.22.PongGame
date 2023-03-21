from turtle import Screen
from Paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong game')
screen.tracer(0)
r_paddle = Paddle()
r_paddle.setpos(x=350, y=0)
l_paddle = Paddle()
l_paddle.setpos(x=-350, y=0)
ball = Ball()
screen.update()

screen.listen()
game_state = True
while True:
    screen.onkey(r_paddle.up, 'Up')
    screen.onkey(r_paddle.down, 'Down')
    screen.onkey(l_paddle.up, 'w')
    screen.onkey(l_paddle.down, 's')
    if ball.distance(r_paddle.pos()) < 45 or ball.distance(l_paddle.pos()) < 45 :
        pass

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if (ball.xcor() > 330 and ball.distance(r_paddle.pos()) < 50) or\
            (ball.xcor() < -330 and ball.distance(l_paddle.pos()) < 50):
        ball.bounce_paddle()

    ball.moving()

    sleep(0.1)
    screen.update()

screen.exitonclick()
