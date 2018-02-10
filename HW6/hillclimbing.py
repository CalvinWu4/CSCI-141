"""
Calvin Wu
purpose: hw solution code
assignment: hill climbing, greedy algorithms
"""

from rit_lib import *
from math import *

class Point3D(struct):
    """
    Creates a class to represent the 3D point
    """
    _slots=((float,'x'),(float,'y'),(float,'z'))

def evaluate(x,y):
    """
    Finds the local maximum given x and y
    :param x:float
    :param y:float
    :return:float
    """
    z=sin(int(x)^2)*2-y*cos(x*y)-x
    return z

def maxPoint(pointList):
    """
    Takes a list of 3D points and returns the 3D point that has the maximum z value
    :param pointList:list
    :return:float
    """
    element=pointList[0]
    maxz=element.z
    maxpoint=0
    for i in (1, len(pointList)-1):
        element=pointList[i]
        z=element.z
        if z>maxz:
            maxz=z
            maxpoint=i
    return maxpoint

def hillClimb(x,y,d):
    """
    This function implements the hill climbing algorithm starting at the position ( x, y )
    The function uses the step distance, d, to generate the neighbors
    :param x:float
    :param y:float
    :param d:float
    :return:string
    """
    count=0
    error=0
    while count<= 300:
        neighbors=[]
        neighbors.append(Point3D(x,y,evaluate(x,y)))
        neighbors.append(Point3D(x-d,y,evaluate(x-d,y)))
        neighbors.append(Point3D(x+d,y,evaluate(x+d,y)))
        neighbors.append(Point3D(x,y-d,evaluate(x,y-d)))
        neighbors.append(Point3D(x,y+d,evaluate(x,y+d)))
        maxpoint = maxPoint(neighbors)
        print("Current point",neighbors[0])
        if maxpoint==0:
            print("Left point:", neighbors[1])
            print("Right point:", neighbors[2])
            print("Bottom point:", neighbors[3])
            print("Top point:", neighbors[4])
            print("Local maximum point is:", neighbors[0])
            return 0
        count+=1
        element=neighbors[maxpoint]
        x=element.x
        y=element.y
    print("Unable to find maximum after 300 iterations")

def main():
    """
    Executes the hillClimb function
    :return:string
    """
    x=float(input("Enter the initial x value:"))
    y=float(input("Enter the initial y value:"))
    d=float(input("Enter the step distance:"))
    hillClimb(x,y,d)
main()



