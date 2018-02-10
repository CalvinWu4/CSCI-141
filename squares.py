"""Calvin Wu"""

import turtle, math

def start():
    """
    pre-conditions: turtle is facing east, turtle speed is 1
    post-conditions: turtle is facing north, turtle speed is 10
    """
    turtle.left(90)
    turtle.speed(10)

def squares(depth, sideLength):
    """
    pre-conditions: No squares are drawn
    post-conditions: Squares are drawn
    """
    if depth == 0:
        pass
    elif depth == 1:
        turtle.forward(sideLength)
        turtle.right(90)
        turtle.forward(sideLength)

        turtle.right(90)
        turtle.forward(sideLength)

        turtle.right(90)
        turtle.forward(sideLength)

    else:
        turtle.forward(sideLength/2)
        turtle.right(45)
        squares(depth-1, (sideLength/2)/math.sqrt(2))
        turtle.right(45)
        turtle.forward(sideLength/2)
        turtle.right(90)
        turtle.forward(sideLength)
        turtle.right(90)
        turtle.forward(sideLength/2)
        turtle.right(45)
        squares(depth-1, (sideLength/2)/math.sqrt(2))
        turtle.right(45)
        turtle.forward(sideLength/2)
        turtle.right(90)
        turtle.forward(sideLength)

def finish():
    """
    pre-conditions: turtle is visible
    post-conditions: turtle is hidden
    """
    turtle.hideturtle()
    turtle.update()

def main():
    """
    pre-conditions: functions are not called
    post-conditions: functions are called, prompts user for the depth value, and closes window when user hits the enter key
    """
    start()
    squares(int(input("enter depth")),200)
    finish()
    input("Hit enter to close...")

main()