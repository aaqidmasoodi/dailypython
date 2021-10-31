import turtle
import time
from init_turtle import initilize_screen, initilize_ball
import os

# system is used for running system command from within the program


# SIMULATION VARIABLE
del_T = 1/120

# Create a screen object
my_scr = initilize_screen()


# create ball
ball = initilize_ball()
ball.dy = -5
ball.dx = 3
ball.bounce_height = 7
ball.shapesize(stretch_len=5, stretch_wid=1)
GRAVITY = 0.1


# platform
platform = turtle.Turtle()
platform.shape('square')
platform.penup()
platform.speed(0)
platform.goto(0,-150)
platform.shapesize(stretch_len=5, stretch_wid=2)
# platform.hideturtle()

# platform.showturtle()

while True:


    ball.sety(ball.ycor() + ball.dy)
    # ball.setx(ball.xcor() + ball.dx)

    ball.dy -= GRAVITY

    # print(ball.dy)

    if ball.ycor() < platform.ycor() + 20: # these can be fine tuned   
        ball.dy = ball.bounce_height
        if ball.bounce_height > 0:
            # os.system('aplay ./Intermediate\ Python/02\ Turtle\ Academy/bounce.wav &')
            ball.bounce_height -= 0.2




    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
 


    my_scr.update()
    time.sleep(del_T)