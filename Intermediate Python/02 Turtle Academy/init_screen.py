import turtle


def initilize_screen(color='lightgreen', width=800, height=600):
    myscreen = turtle.Screen()
    myscreen.setup(width=width, height=height)
    myscreen.bgcolor(color)
    myscreen.tracer(0)

    return myscreen