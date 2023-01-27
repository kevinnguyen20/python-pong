import turtle

class Ball():
    def __init__(self):
        self.ball=turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx=0.1
        self.ball.dy=0.1

    def move(self):
        self.ball.setx(self.ball.xcor()+self.ball.dx)
        self.ball.sety(self.ball.ycor()+self.ball.dy)
