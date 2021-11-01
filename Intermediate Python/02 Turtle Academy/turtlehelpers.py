import turtle



def init_screen(color='lightgreen', width=800, height=600):
    myscreen = turtle.Screen()
    myscreen.setup(width=width, height=height)
    myscreen.bgcolor(color)
    myscreen.tracer(0)

    return myscreen



def create_ball(shape='circle', speed=0):
    ball = turtle.Turtle()
    ball.shape(shape)
    ball.penup()
    ball.speed(speed)

    return ball



def create_paddle(shape='square', speed=0, placement='horizontal'):
    
    paddle = turtle.Turtle()
    paddle.shape(shape)
    paddle.penup()
    paddle.speed(speed)
    paddle.shapesize(
        stretch_len = 5 if placement == 'horizontal' else 1,
        stretch_wid = 5 if placement == 'vertical' else 1
    )

    return paddle