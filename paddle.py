import turtle

class Paddle():

    def __init__(self,x_pos):
        self.paddle=turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x_pos,0)

    def paddle_up(self):
        y=self.paddle.ycor()
        y+=20
        self.paddle.sety(y)

    def paddle_down(self):
        y=self.paddle.ycor()
        y-=20
        self.paddle.sety(y)
