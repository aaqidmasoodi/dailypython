import turtle


def initilize_screen(color='lightgreen', width=800, height=600):
    myscreen = turtle.Screen()
    myscreen.setup(width=width, height=height)
    myscreen.bgcolor(color)
    myscreen.tracer(0)

    return myscreen

# shapesize(stretch_len=, stretch_wid=)

def initilize_ball(color='red'):
    myball = turtle.Turtle()
    myball.shape('circle')
    myball.penup()
    myball.speed(0)
    myball.color(color) # change the color

    return myball
