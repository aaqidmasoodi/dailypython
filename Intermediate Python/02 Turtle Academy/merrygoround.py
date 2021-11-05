import turtle
import helper as hlp
import time

rotations = 0
scr = hlp.init_screen()


ball = hlp.create_ball()
ball.goto(-200,200)


movement = 10

ball.dx = movement
ball.dy = 0






pen = turtle.Turtle()
pen.hideturtle()
pen.goto(250,250)
 # turtle DOcs




while True:

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    

    if ball.xcor() == 200:
        ball.dx = 0
        ball.dy = -movement

        
    if ball.ycor() == -200:
        ball.dx = -movement
        ball.dy = 0


    if ball.xcor() == -200:
        ball.dx = 0
        ball.dy = movement

    if ball.ycor() == 200 and ball.xcor() == -200:
        ball.dx = movement
        ball.dy = 0
        rotations += 1
        

        
    pen.clear()
    pen.write(f'({ball.xcor()},{ball.ycor()})', font=('OpenSans',25,'bold'), align='center')    
        


    scr.update()
    time.sleep(1/60)
