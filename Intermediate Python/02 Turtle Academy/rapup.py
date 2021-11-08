import turtle
import helper as hlp
import time
import random
import math

scr = hlp.init_screen()


# player object

player = hlp.create_shape(shape='square', color='darkblue')


movement = 2
player.dx = movement
player.dy = 0


# food object

food = hlp.create_shape(shape='circle', color='red')


# writer
writer = turtle.Turtle()




# create functions to make it move in a certain direction

def move_right():
    player.dx = movement
    player.dy = 0

def move_left():
    player.dx = -movement
    player.dy = 0

def move_up():
    player.dx = 0
    player.dy = movement

def move_down():
    player.dx = 0
    player.dy = -movement

# check food and player collison


def is_collision(player, food):
    distance = math.sqrt(math.pow(food.xcor() - player.xcor(), 2) + math.pow(food.ycor() - player.ycor(), 2))
    writer.clear()
    writer.write(f'{int(distance)}', font=('OpenSans',50))
    if distance < 20:
        return True

    return False


scr.listen()
scr.onkeypress(move_right, 'd')
scr.onkeypress(move_left, 'a')
scr.onkeypress(move_up, 'w')
scr.onkeypress(move_down, 's')




while True:


    # move the player

    player.setx(player.xcor() + player.dx)
    player.sety(player.ycor() + player.dy)


    # egde wrap

    if player.xcor() > 400:
        player.setx(-400)

    if player.xcor() < -400:
        player.setx(400)

    if player.ycor() > 300:
        player.sety(-300)

    if player.ycor() < -300:
        player.sety(300)



    if is_collision(player, food):
        print('collision')

        


    scr.update()
    time.sleep(1/240)



