from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
my_screen = Screen()
my_screen.tracer(0)
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("Pong Game")
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
my_screen.listen()
my_screen.onkey(key="Up", fun=r_paddle.moving_up)
my_screen.onkey(key="Down", fun=r_paddle.moving_down)
my_screen.onkey(key="w", fun=l_paddle.moving_up)
my_screen.onkey(key="s", fun=l_paddle.moving_down)
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.moving()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle.paddle) < 40 and ball.xcor() > 320) or (
            ball.distance(l_paddle.paddle) < 40 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        score.r_point()
my_screen.exitonclick()
