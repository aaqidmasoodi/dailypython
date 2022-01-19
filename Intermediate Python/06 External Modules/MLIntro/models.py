import turtle


# CONSTANTS
WINDOW_TITLE_DEFAULT = '#DailyPython'
WINDOW_BACKGROUND_COLOR_DEFAULT = '#111111'
WINDOW_WIDTH_DEFAULT = 800
WINDOW_HEIGHT_DEFAULT = 600
MODEL_FOREGROUND_COLOR_DEFAULT = '#EEEEEE'
MODEL_SHAPE_DEFAULT = 'square'



def window(

        width=WINDOW_WIDTH_DEFAULT,
        height=WINDOW_HEIGHT_DEFAULT,
        title=WINDOW_TITLE_DEFAULT,
        color=WINDOW_BACKGROUND_COLOR_DEFAULT,
        tracer=0,

    ):


    win = turtle.Screen()
    win.setup(width=width, height=height)
    win.title(title)
    win.bgcolor(color)
    win.tracer(tracer)

    return win




def shape(
        type=MODEL_SHAPE_DEFAULT,
        stretch_wid=1,
        stretch_len=1,
        color=MODEL_FOREGROUND_COLOR_DEFAULT,
        is_pen=False,
        speed=0,
        x = 0,
        y = 0,
    ):

    rect = turtle.Turtle()
    rect.shape(type)
    rect.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
    rect.color(color)
    if not is_pen:
        rect.penup()
    rect.speed(speed)
    rect.goto(x,y)


    return rect





