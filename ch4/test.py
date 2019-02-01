import turtle
myWindow = turtle.Screen()
myTurtle = turtle.Turtle()
myWindow.reset()
myWindow.setworldcoordinates(-50, -7.5, 50, 7.5)
for _ in range(72):
    myTurtle.left(10)

for _ in range(8):
    myTurtle.left(45); myTurtle.fd(2)



myWindow.exitonclick()