import helper as hlp
import time


scr = hlp.init_screen()


ball = hlp.create_ball()
ball.dx = 1
ball.dy = 1
ball.goto(200,200)


# paddle A
paddle_a = hlp.create_paddle(placement='vertical',color='purple')
paddle_a.goto(-350, 0)


# paddle B
paddle_b = hlp.create_paddle(placement='vertical',color='purple')
paddle_b.goto(350, 0)




# EVENT LISTENER
# EVENTS --- >> mouseclicks , keypressed, movement , 

def paddle_a_up():

    if paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 20)
    

def paddle_a_down():
    if paddle_a.ycor() > -250:
        paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    if paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    if paddle_b.ycor() > -250:
        paddle_b.sety(paddle_b.ycor() - 20)


# handling events
# HOW DO YOU KNOW KI AISEHI KRNA H?
scr.listen()
# THE MOST IMPORTANT THING OF ALL
scr.onkeypress(paddle_a_up, 'W') # None
scr.onkeypress(paddle_a_down, 's') # DO NOT CALL THE FUNCTION
scr.onkeypress(paddle_b_up, 'Up')
scr.onkeypress(paddle_b_down, 'Down')



def is_colliding_paddle_b():

    paddle_b_collision_conditions = [

        ball.xcor() > paddle_b.xcor() - 20,
        ball.ycor() < paddle_b.ycor() + 50,
        ball.ycor() > paddle_b.ycor() - 50,
    ]

    if all(paddle_b_collision_conditions):
        return True

    return False



def is_colliding_paddle_a():

    paddle_a_collision_conditions = [

        ball.xcor() < paddle_a.xcor() + 20,
        ball.ycor() < paddle_a.ycor() + 50,
        ball.ycor() > paddle_a.ycor() - 50,
    ]

    if all(paddle_a_collision_conditions):
        return True

    return False




while True:

    # Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)



    # bounderies 

    if ball.ycor() >290:
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() >390 or ball.xcor() < -390:
        ball.dx *= -1
        ball.goto(0,0)




    # Readibility and clean code
    if is_colliding_paddle_b():
        ball.dx *= -1

    elif is_colliding_paddle_a():
        ball.dx *= -1




    scr.update()
    time.sleep(1/240)





# TRY TO IMPLEMENT THE SCORING MECHANICSM FOR PONG