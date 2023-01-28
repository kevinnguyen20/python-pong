import math
import turtle
import winsound
from functools import partial
import random

# Paddles
def init_paddle(x_pos):
    paddle=turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5,stretch_len=1)
    paddle.penup()
    paddle.goto(x_pos,0)
    
    return paddle

def paddle_up(paddle):
    y=paddle.ycor()
    y+=20
    paddle.sety(y)

def paddle_down(paddle):
    y=paddle.ycor()
    y-=20
    paddle.sety(y)

# Ball
def init_ball():
    ball=turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx=0.1
    ball.dy=0.1

    return ball

def move(ball):
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

# Pen
def init_pen():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.player1=0
    pen.player2=0
    pen.write("Player A: {}  Player B: {}".format(pen.player1,pen.player2), align="center", font=("Courier", 24, "normal"))

    return pen

# Border checking
def greater_than_x(ball,pen):
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        pen.player1+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(pen.player1,pen.player2),align="center",font=("Courier", 24, "normal"))

def smaller_than_x(ball,pen):
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        pen.player2+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(pen.player1,pen.player2),align="center",font=("Courier", 24, "normal"))

def check_border_x(ball,pen):
    greater_than_x(ball,pen)
    smaller_than_x(ball,pen)

def greater_than_y(ball):
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

def smaller_than_y(ball):
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

def check_border_y(ball):
    greater_than_y(ball)
    smaller_than_y(ball)

def check_border(ball,pen):
    check_border_x(ball,pen)
    check_border_y(ball)

# Paddle and ball collision
def collision_paddle_player1(paddle,ball):
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle.ycor()+40 and ball.ycor()>paddle.ycor()-40):
        ball.setx(-340)
        ball.dy=math.copysign(random.random()/20 + 0.075,ball.dy)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

def collision_paddle_player2(paddle,ball):
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle.ycor()+40 and ball.ycor()>paddle.ycor()-40):
        
        ball.setx(340)
        ball.dy=math.copysign(random.random()/20 + 0.075,ball.dy)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

# Main game loop
def mainloop(wn,paddle_player1,paddle_player2,ball,pen):
    while True:
        wn.update()

        # Move the ball
        move(ball)

        # Check border
        check_border(ball,pen)

        # Check collision ball and paddle
        collision_paddle_player1(paddle_player1,ball)
        collision_paddle_player2(paddle_player2,ball)

def close(wn):
    wn.bye()

def main():
    wn=turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Initialization
    paddle_player1=init_paddle(-350)
    paddle_player2=init_paddle(350)
    ball=init_ball()
    pen=init_pen()

    # Keyboard binding
    wn.listen()

    func1=partial(paddle_up,paddle_player1)
    func2=partial(paddle_down,paddle_player1)
    func3=partial(paddle_up,paddle_player2)
    func4=partial(paddle_down,paddle_player2)
    wn.onkeypress(func1,"w")
    wn.onkeypress(func2,"s")
    wn.onkeypress(func3,"Up")
    wn.onkeypress(func4,"Down")

    # Close window
    func=partial(close,wn)
    wn.onkeypress(func, "Escape")

    # Game mainloop
    mainloop(wn,paddle_player1,paddle_player2,ball,pen)

if __name__ == "__main__":
    main()
