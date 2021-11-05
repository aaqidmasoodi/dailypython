import turtle


scr = turtle.Screen()
scr.tracer(1)




tut = turtle.Turtle()
tut.penup()


tut.forward(100)

tut.goto(250,250)
tut.goto(-250,250)
tut.goto(500,500)


while True:


    scr.update()