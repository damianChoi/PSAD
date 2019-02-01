import turtle
myTurtle = turtle.Turtle()
myWindow = turtle.Screen()
myWindow.tracer(1, 1000)
dist = 2
for i in range(200):
    myTurtle.fd(dist)
    myTurtle.rt(90)
    dist += 2

myWindow.exitonclick()