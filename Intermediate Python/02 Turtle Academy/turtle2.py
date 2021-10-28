import turtle 
import time

# window
screen = turtle.Screen()
screen.title('Creating a ball')
screen.bgcolor('orange')
screen.setup(width=800, height=600)
screen.tracer(0) # killing the animation




# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle') # so that it looks like a ball


while True:
    
    print('Hello')
    ball.setx(ball.xcor() + 1) # do you understand what this is doing?
   # travelling speed is not fixed?
    
    screen.update()
    time.sleep(1/60) # your thread will sleep for 1 second
    # limit the iteration rate
    # less burden on system

    