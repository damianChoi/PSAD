def tree(branchLen, t, r):
    if branchLen > 5:
        t.pencolor('brown')
        if branchLen <= 30:
            t.pencolor('green')
        t.width(branchLen//10)
        t.forward(branchLen)
        if branchLen <= 20:
            t.dot(10, "red");
        angle = r.randrange(15, 45)
        t.right(angle)
        tree(branchLen-r.randrange(15, 30), t, r)
        t.left(2*angle)
        tree(branchLen-r.randrange(15, 30), t, r)
        t.right(angle)
        t.backward(branchLen)

def main():
    import turtle, random
    r = random
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.shape('turtle')
    tree(75, t, r)
    myWin.exitonclick()

main()

