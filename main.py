from turtle import Screen
from Paddle import Paddle
from time import sleep

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong game')
screen.tracer(0)
user_paddle = Paddle()
user_paddle.setpos(x=350, y=0)
screen.update()

screen.listen()
while True:
    screen.onkey(user_paddle.up, 'w')
    screen.onkey(user_paddle.down, 's')
    sleep(0.15)
    screen.update()

screen.exitonclick()
