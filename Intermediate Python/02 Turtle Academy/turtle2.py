import turtle 
import time

# window
screen = turtle.Screen()
screen.title('Creating a ball')
screen.bgcolor('orange')
screen.setup(width=800, height=600)
screen.tracer(0) # killing the animation




# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle') # so that it looks like a ball
ball.penup()


dx = 5
dy = 5


# Main Loop
while True:
    

    # Moving the ball
    # set the x # get the x
    ball.setx(ball.xcor() + dx) # varibles
    ball.sety(ball.ycor() + dy) 

    # print((int(ball.xcor()), int(ball.ycor())))

    if ball.ycor() == 290 or ball.ycor() == -290:
        dy = -dy
 

    if ball.xcor() == -390 or ball.xcor() == 390:
        dx = -dx




    screen.update()
    time.sleep(1/60) 
 

    