import turtle


# Screen
screen = turtle.Screen()
screen.bgcolor('lightgreen')
screen.title('TurtleGraphics - CodeWithAaqid')
screen.setup(800,600)




# Turtle
myturtle = turtle.Turtle()


for i in range(20):
    for i in range(4):
        myturtle.forward(100)
        myturtle.left(90)

    myturtle.left(18)




while True:
    screen.update()