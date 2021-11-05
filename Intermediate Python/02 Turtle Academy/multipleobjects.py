import turtle
import time
import random


screen = turtle.Screen()
screen.tracer(0)
screen.setup(800,600)


myturtles = []


for i in range(500):
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.color(random.choice(['red','blue','black','orange','lightgreen']))
    ball.penup()
    ball.goto(random.randint(-200,200),random.randint(-200,200))
    ball.speed(0)
    ball.dx = random.choice([10,-10])
    ball.dy = random.choice([10,-10])
    ball.shapesize(stretch_len=0.2, stretch_wid=0.2)
    myturtles.append(ball)



   







while True:


    for ball in myturtles:
        ball.setx(ball.xcor() +  ball.dx)
        ball.sety(ball.ycor() +  ball.dy)



        if ball.ycor() > 300 or ball.ycor() < -300:
            ball.dy *= -1

        if ball.xcor() > 400 or ball.xcor() < -400:
            ball.dx *= -1


    screen.update()



# try to implement logic such that a single brick will break on two hits
# THE POWER OF ORIITENTED