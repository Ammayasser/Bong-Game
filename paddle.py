from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(position)

        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    def moving_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def moving_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
