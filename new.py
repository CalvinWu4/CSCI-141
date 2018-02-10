# import turtle
#
# def drawSquares(length,depth):
#     turtle.speed(10)
#     if depth<=0:
#         return
#     count=4
#     while count>0:
#         turtle.forward(length)
#         turtle.left(90)
#         drawSquares(length/2,depth-1)
#         turtle.right(180)
#         count-=1
#
# drawSquares(100,3
#             )
# input('enter to close')

from turtle import *

def f(length, depth):
   speed(10)
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
f(200, 3)
input('enter to close')

