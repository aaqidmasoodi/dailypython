import helper as hlp
import time
import os



scr = hlp.init_screen()



ball = hlp.create_shape(shape='circle')
ball.dy = -1


bounce_height = 15

while True:


    ball.sety(ball.ycor() + ball.dy)
    # ball.setx(ball.xcor() + 1)


    ball.dy -= 0.5 # gravity


    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy = bounce_height
        if bounce_height > 0:
            bounce_height -= 0.2
            os.system('aplay /home/neo/Documents/Workshop/dailypython/Intermediate\ Python/02\ Turtle\ Academy/bounce.wav &')



    scr.update()
    time.sleep(1/60)