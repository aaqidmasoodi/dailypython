import turtle
import helper as hlp
import time
import random

scr = hlp.init_screen()
scr.tracer(0)



item = turtle.Turtle()
item.shape('square')
item.color('blue')
item.speed(0)
item.penup()

def magic(x,y):

    item.hideturtle()


scr.listen()

item.onclick(magic, btn=1)



while True:




    scr.update()
    time.sleep(1/120)