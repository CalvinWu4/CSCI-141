"""Calvin Wu"""

import turtle, random, math

def MAX_FIGURES():
    """ Maximum number of individual figure elements. """
    return 500

def MAX_DISTANCE():
    """ Maximum distance between the starting points of two figure elements. """
    return 30

def MAX_ANGLE():
    """Absolute value of the angle the turtle turns before moving to the starting position for the next figure element."""
    return 30

def MAX_SIZE():
    """Individual sizes should be integers between 1 and MAX_SIZE inclusive."""
    return 30

def BOUNDING_BOX():
    """Draws the boundary box"""
    turtle.up()
    turtle.setpos(0,0)
    turtle.setheading(90)
    turtle.forward(100)
    turtle.color("black")
    turtle.down()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.up()
    turtle.setpos(0,0)
    turtle.setheading(90)

def drawFiguresRec(n,area):
    """Makes a triangle trail recursively, adding up the painted areas, and keeping inside the boundary box"""
    n2=n
    if n2 <= 0:
        print("The total painted area is " + str(area) + " units")
        turtle.hideturtle()
        turtle.update()
    else:
        n=random.randint(0,MAX_FIGURES())
        d=random.randint(1,MAX_DISTANCE())
        a=random.randint(-MAX_ANGLE(),MAX_ANGLE())
        s=random.randint(1,MAX_SIZE())
        area += (math.sqrt(3)/4)*(s^2)
        turtle.color(random.random(),random.random(), random.random())
        turtle.begin_fill()
        turtle.down()
        turtle.forward(s)
        turtle.left(120)
        turtle.forward(s)
        turtle.left(120)
        turtle.forward(s)
        turtle.back(s)
        turtle.end_fill()
        turtle.right(60)
        turtle.up()
        turtle.left(a)
        turtle.forward(d)
        if math.fabs(turtle.xcor()) > 100 or math.fabs(turtle.ycor()) > 100:
            turtle.setheading(turtle.towards(0,0))
            turtle.forward(30)
        else:
            pass
        drawFiguresRec(n2-1,area)

def drawFiguresIter(n):
    """Makes a triangle trail iteratively, adding up the painted areas, and keeping the triangles inside the boundary box"""
    area=0
    for i in range(0,n):
        n2=n
        n2=random.randint(0,MAX_FIGURES())
        d=random.randint(1,MAX_DISTANCE())
        a=random.randint(-MAX_ANGLE(),MAX_ANGLE())
        s=random.randint(1,MAX_SIZE())
        area += (math.sqrt(3)/4)*(s^2)
        turtle.color(random.random(),random.random(), random.random())
        turtle.begin_fill()
        turtle.down()
        turtle.forward(s)
        turtle.left(120)
        turtle.forward(s)
        turtle.left(120)
        turtle.forward(s)
        turtle.back(s)
        turtle.end_fill()
        turtle.right(60)
        turtle.up()
        turtle.left(a)
        turtle.forward(d)
        if math.fabs(turtle.xcor()) > 100 or math.fabs(turtle.ycor()) > 100:
            turtle.setheading(turtle.towards(0,0))
            turtle.forward(30)
        else:
            pass
    print("The total painted area is " + str(area) + " units")

def main():
    """Prompts user for number of figures, checks if it is in valid range, if not it pops an error message and exits the window but if so it calls BOUNDING_BOX and drawFiguresRec, waits for
    the user to hit enter, clears the screen, calls BOUNDING_BOX and drawFiguresIter, waits for user to press enter, and exits the window"""
    turtle.speed(10)
    n=int(input("Enter number of figures"))
    if n<0 or n> MAX_FIGURES():
        print("Error: The valid range for the number of triangles is between 0 and 500 inclusive")
        turtle.bye()
    else:
        BOUNDING_BOX()
        drawFiguresRec(n,0)
        input("Hit enter to do iteration")
        turtle.clear()
        turtle.showturtle()
        BOUNDING_BOX()
        drawFiguresIter(n)
        turtle.hideturtle()
        turtle.update()
        input("Hit enter to close")
main()