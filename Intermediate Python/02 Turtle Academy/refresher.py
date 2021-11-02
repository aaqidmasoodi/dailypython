import turtle
import time
scr = turtle.Screen()
scr.setup(800,600)
scr.bgcolor('orange')
scr.title('Refresher')
scr.tracer(0)




trt = turtle.Turtle()
trt.penup()
trt.speed(0)

dx = 2
dy = 2



while True:

    # literals
    trt.setx(trt.xcor() + dx) # this statement says ... set the x to whatever it is right now plus 1 
    trt.sety(trt.ycor() + dy)


    if trt.ycor() > 300:
        dy *= -1


    if trt.xcor() > 400: 
        dx *= -1

    
    if trt.ycor() < -300:
        dy *= -1


    if trt.xcor() < -400:
        dx *= -1


    scr.update()
    time.sleep(1/60)


