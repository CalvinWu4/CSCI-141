"""
file: boxAndWhisker.py
description: This is a program which can draw a box-and-whisker plot.
trending words between a given starting and ending year.
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 12/04/2015
"""

from turtle import *
from rit_lib import *
from wordData import *

def boxAndWhisker(small,q1,med,q3,large):
    """
    Draws a box-and-whisker plot given values for the minimum, first quartile, median, third quartile, and maximum.
    :param small:
    :param q1: int
    :param med: int
    :param q3: int
    :param large: int
    :return: None
    """
    scale=(large-small)*.5
    small=small/scale
    q1=q1/scale
    med=med/scale
    q3=q3/scale
    large=large/scale
    height=.75
    setworldcoordinates(-5,-5,5,5)
    speed(10)
    left(90)
    forward(height)
    back(height)
    left(90)
    forward(med-q1)
    right(90)
    forward(height)
    left(90)
    forward(med-small-(med-q1))
    right(90)
    forward(height/4)
    back(height/2)
    forward(height/4)
    right(90)
    forward(med-small-(med-q1))
    left(90)
    forward(height)
    right(90)
    forward(med-q1)
    right(90)
    forward(height)
    back(height)
    left(90)
    forward(q3-med)
    right(90)
    forward(height)
    left(90)
    forward(large-med-(q3-med))
    left(90)
    forward(height/4)
    back(height/2)
    forward(height/4)
    left(90)
    forward(large-med-(q3-med))
    left(90)
    forward(height)
    right(90)
    forward(q3-med)
    hideturtle()
    done()

if __name__ == '__main__':
    small=int(input('Enter the minimum: '))
    q1=int(input('Enter the first quartile: '))
    med=int(input('Enter the median: '))
    q3=int(input('Enter the third quartile: '))
    large=int(input('Enter the maximum: '))
    boxAndWhisker(small,q1,med,q3,large)