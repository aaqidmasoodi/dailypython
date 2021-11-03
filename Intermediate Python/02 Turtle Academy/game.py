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





while True:
    scr.update()