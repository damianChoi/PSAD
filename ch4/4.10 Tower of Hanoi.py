def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(height, fromPole, toPole):
    print("moving disk", height, "from", fromPole, "to", toPole)

moveTower(3, "A", "B", "C")