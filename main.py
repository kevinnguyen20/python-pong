import turtle
import winsound

import paddle
import ball
import pen

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_player1 = 0
score_player2 = 0

# Paddles
paddle_player1=paddle.Paddle(-350)
paddle_player2=paddle.Paddle(350)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_player1.paddle_up,"w")
wn.onkeypress(paddle_player1.paddle_down,"s")
wn.onkeypress(paddle_player2.paddle_up,"Up")
wn.onkeypress(paddle_player2.paddle_down,"Down")

# Ball
ball_=ball.Ball()

# Pen
pen_=pen.Pen()

# Border checking
def greater_than_x(ball,pen):
    global score_player1
    global score_player2
    if ball.ball.xcor()>390:
        ball.ball.goto(0,0)
        ball.ball.dx*=-1
        score_player1+=1
        pen.pen.clear()
        pen.pen.write("Player A: {}  Player B: {}".format(score_player1, score_player2),align="center",font=("Courier", 24, "normal"))

def smaller_than_x(ball,pen):
    global score_player1
    global score_player2
    if ball.ball.xcor()<-390:
        ball.ball.goto(0,0)
        ball.ball.dx*=-1
        score_player2+=1
        pen.pen.clear()
        pen.pen.write("Player A: {}  Player B: {}".format(score_player1, score_player2),align="center",font=("Courier", 24, "normal"))

def check_border_x(ball,pen):
    greater_than_x(ball,pen)
    smaller_than_x(ball,pen)

def greater_than_y(ball):
    if ball.ball.ycor()>290:
        ball.ball.sety(290)
        ball.ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

def smaller_than_y(ball):
    if ball.ball.ycor()<-290:
        ball.ball.sety(-290)
        ball.ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

def check_border_y(ball):
    greater_than_y(ball)
    smaller_than_y(ball)

def check_border(ball,pen):
    check_border_x(ball,pen)
    check_border_y(ball)

# Paddle and ball collision
def collision_paddle_player1(paddle,ball):
    if (ball.ball.xcor()<-340 and ball.ball.xcor()>-350) and (ball.ball.ycor()<paddle.paddle.ycor()+40 and ball.ball.ycor()>paddle.paddle.ycor()-40):
        ball.ball.setx(-340)
        ball.ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

def collision_paddle_player2(paddle,ball):
    if (ball.ball.xcor()>340 and ball.ball.xcor()<350) and (ball.ball.ycor()<paddle.paddle.ycor()+40 and ball.ball.ycor()>paddle.paddle.ycor()-40):
        ball.ball.setx(340)
        ball.ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball_.move()

    # Check border
    check_border(ball_,pen_)

    # Check collision ball and paddle
    collision_paddle_player1(paddle_player1,ball_)
    collision_paddle_player2(paddle_player2,ball_)
