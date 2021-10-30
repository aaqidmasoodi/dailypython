import turtle
import time
from init_screen import initilize_screen


# SIMULATION VARIABLE
FPS = 1/120

# Create a screen object
my_scr = initilize_screen()




# create ball
ball = turtle.Turtle()
ball.shape('circle')
ball.penup()
ball.color('red')
ball.speed(0)
ball.dy = -5
ball.dx = 3
GRAVITY = 0.1


while True:


    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    ball.dy -= GRAVITY

    # print(ball.dy)

    if ball.ycor() < -290:
        ball.dy = 7


    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
 


    my_scr.update()
    time.sleep(FPS)