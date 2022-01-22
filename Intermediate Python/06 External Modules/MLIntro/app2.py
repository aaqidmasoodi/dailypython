import models
import time


# Main Window
screen = models.window()

# Borders
border_top = models.shape(stretch_len=800//20, x=0, y=290)
border_bottom = models.shape(stretch_len=800//20, x=0, y=-290)

# Ball
ball = models.shape(type='circle')
ball.dx = 2
ball.dy = 2

# paddle A
paddle_a = models.shape(stretch_wid=5, x=-360)


# paddle B
paddle_b = models.shape(stretch_wid=5, x=360)


# player spaddle movement
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 40)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 40)


def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 40)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 40)


# 40 8000

# event binding
screen.listen()
screen.onkeypress(paddle_a_up, 'w')
screen.onkeypress(paddle_a_down, 's')
screen.onkeypress(paddle_b_up, 'Up')
screen.onkeypress(paddle_b_down, 'Down')



f = open('game_data.csv', 'w')


f.write(f'x,y,dx,dy,paddley\n')



while True:

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # check borders

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.dy *= -1

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
        ball.goto(0,0)

    # paddle collision

    if ball.xcor() < paddle_a.xcor() + 20 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
    elif ball.xcor() > paddle_b.xcor() - 20 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1



    f.write(f'{ball.xcor()},{ball.ycor()},{ball.dx},{ball.dy},{paddle_a.ycor()}\n')

    screen.update()
    time.sleep(1/120)