# Call Back
# being as a first class citizen




import turtle


scr = turtle.Screen()
scr.tracer(0)



def create_turtle(x,y):
    tut = turtle.Turtle()
    tut.penup()
    tut.shape('circle')
    tut.goto(x,y)

    




scr.onclick(create_turtle)

# 1 left mouse
# 2 middle mouse
# 3 right mouse


while True:


    

    scr.update()
