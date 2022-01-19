import models
import time
import joblib
import pandas as pd

model = joblib.load('pongAI2.joblib')

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


ball_info = pd.DataFrame(columns=['x','y','dx','dy'])


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


    to_predict = ball_info.append({
        'x':ball.xcor(),
        'y':ball.ycor(),
        'dx':ball.dx,
        'dy':ball.dy
    }, ignore_index=True)
    

    new_y = model.predict(to_predict)

    print(new_y)

    # paddle_a.sety(int(new_y))

    # paddle_a.sety(ball.ycor()) # why this cannot?


    screen.update()
    time.sleep(1/120)
