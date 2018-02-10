"""Calvin Wu"""
import turtle

def init(rings):
    turtle.reset()
    turtle.left(90)
    turtle.setup(600,600)
    turtle.penup()
    turtle.setpos(0,rings*-20)
    turtle.pendown()
    turtle.speed(0)
def drawBullseyeIter(rings):
    area=0
    while rings > 0:
        turtle.speed(10)
        turtle.down()
        if rings%3==0:
            turtle.color("blue")
        elif rings%3==1:
            turtle.color("red")
        else:
            turtle.color("black")
        turtle.begin_fill()
        turtle.circle(20*rings)
        turtle.end_fill()
        area+=20*rings*20*rings*3.14
        turtle.up()
        rings-=1
        print("Total area is " + str(area))

def drawBullseyeRec(rings,area=0):
    if rings == 0:
        pass
    else:
        turtle.speed(10)
        if rings%3==0:
            turtle.color("blue")
        elif rings%3==1:
            turtle.color("red")
        else:
            turtle.color("black")
        turtle.down()
        turtle.begin_fill()
        turtle.circle(20*rings)
        area+=20*rings*20*rings*3.14
        turtle.end_fill()
        turtle.up()
        drawBullseyeRec(rings-1)
        print("Total area is " + str(area))
drawBullseyeRec(6)
input('go to iteration')
init()
drawBullseyeIter(6)
input('enter to close')




