import turtle
import math


def init_screen(width=800, height=600, color='lightgreen', title='#DailyPython', tracer=0):
    win = turtle.Screen()
    win.setup(width=width, height=height)
    win.bgcolor(color)
    win.title(title)
    win.tracer(tracer) # No Aimation for Turtle

    return win



def create_shape(shape='circle', color='blue', speed=0):
    ball = turtle.Turtle()
    ball.shape(shape)
    ball.color(color)
    ball.penup()
    ball.speed(speed)

    return ball


def create_paddle(shape='square', speed=0, color='brown', placement='horizontal'):
    paddle = turtle.Turtle()
    paddle.shape(shape)
    paddle.color(color)
    paddle.shapesize(
        
        stretch_len = 5 if placement == 'horizontal' else 1,
        stretch_wid = 5 if placement == 'vertical' else 1
     
    )

    paddle.penup()
    paddle.speed(speed)
    

    return paddle




def get_distance(object1, object2):

    distance = math.sqrt(
        math.pow(object2.xcor() - object1.xcor(), 2) + \
        math.pow(object2.ycor() - object1.ycor(), 2))
        
    return distance