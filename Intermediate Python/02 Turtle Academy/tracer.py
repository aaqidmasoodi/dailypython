import turtle


scr = turtle.Screen()
scr.tracer(0)



tut = turtle.Turtle()
tut.penup()


tut.forward(100)

tut.goto(250,250)
tut.goto(-250,250)
tut.goto(500,500)



tut.setx(0)
tut.sety(0)

while True:


    scr.update()