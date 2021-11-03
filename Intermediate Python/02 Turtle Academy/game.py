import turtle
import helper as hlp




scr = hlp.init_screen()



ball = hlp.create_ball()
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

    paddle_a.sety(paddle_a.ycor() + 20)
    


def paddle_a_down():

    paddle_a.sety(paddle_a.ycor() - 20)


# handling events
# HOW DO YOU KNWO THIS KI AISE H RNA H YE?
scr.listen()
# THE MOST IMPORTANT THING OF ALL
scr.onkeypress(paddle_a_up, 'w') # None
scr.onkeypress(paddle_a_down, 's') # DO NOT CALL THE FUNCTION



print(paddle_a.ycor())


while True:
    scr.update()