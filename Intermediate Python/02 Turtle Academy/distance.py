import turtle
import time
import math

scr = turtle.Screen()
scr.bgcolor('black')
scr.setup(width=800,height=600)
scr.title('Ball Collison')
scr.tracer(0)


balls = []


ball_dx = [2,-2] 
ball_coordinates = [(200,200), (-200,200)]

for i in range(2):
    balls.append(turtle.Turtle())


for i, ball in enumerate(balls):
    ball.shape('circle')
    ball.color('white')
    ball.penup()
    ball.speed(0)
    ball.goto(ball_coordinates[i])
    ball.dx = ball_dx[i]
    ball.dy = 2


def is_collision(balls):
    ball1, ball2 = balls


    distance = math.sqrt(
        
        math.pow((ball2.xcor() - ball1.xcor()),2)  +  
        math.pow((ball2.ycor() - ball1.ycor()), 2)
        
        )

    if distance < 21:
        return True

    return False


while True:

    for ball in balls:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Top and bottom 
        if ball.ycor() > 300 or ball.ycor() < -300:
            ball.dy *= -1


        # left and right
        if ball.xcor() > 400 or ball.xcor() < -400:
            ball.dx *= -1


        if is_collision(balls):
            ball.dx *= -1
            # ball.dy *= -1



    scr.update()
    time.sleep(1/60)


