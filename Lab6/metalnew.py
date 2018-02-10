"""
Author: Sean Strout (sps@cs.rit.edu)
Author: ben k steele (bks@cs.rit.edu)
Author: Calvin Wu

This class represents the types of metal bars that Greedo can
store in his satchel.  Each type of bar is a separate Metal
object.  This module also has routines that work with metals,
e.g. creation, reading from a file, and sorting based on 
various criteria.

Language: Python 3
"""

from rit_lib import *            # rit_lib class

class Metal(struct):
    """
    Represents a single metal type, composed of:
    :slot name (str): The name of the metal
    :slot totalBars (int): The total number of bars
    :slot weightPerBar (int): The weight of a single bar
    :slot valuePerBar (int): The value of a single bar
    :slot valuePerWeight (float): The value per weight of the metal
    :slot barsTaken (int): The number of bars added to the satchel
    """
    _slots=((str, "name"), (int, "totalBars"), (int, "weightPerBar"), (int, "valuePerBar"), (float, "valuePerWeight"), (int, "barsTaken"))


def createMetal(name, totalBars, weightPerBar, valuePerBar):
    """
    Create and return a new Metal object.
    :param name (str): The name of the metal
    :param totalBars (int): The total number of bars
    :param weightPerBar (int): The weight of a single bar
    :param valuePerBar (int): The value of a single bar
    :return: A newly initialized Metal object
    :rtype: Metal
    """
    return Metal(name, totalBars, weightPerBar, valuePerBar, valuePerBar/weightPerBar, 0)

def readMetals(fileName):
    """
    Read the metals from a file whose format is:
        metalName totalBars weightPerBar valuePerBar
    :param fileName (str): The name of the file
    :return: A list of Metal objects
    :rtype: list
    """
    Metals=[]
    with open(fileName) as f:
        for line in f:
            metal=line.split()
            metalOne=createMetal(metal[0], int(metal[1]), int(metal[2]), int(metal[3]))
            Metals.append(metalOne)
        return Metals


def sortMetalsByValuePerBar(metals):
    """
    Sort the metals by value per bar using insertion sort.  The list of
    metals is modified in place to be ordered by value per bar.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """
    for i in range (1, len(metals)):
        t=i
        metalc=metals[t-1]
        valuec=metalc.valuePerBar
        metal=metals[t]
        curValue=metal.valuePerBar
        while(curValue>valuec and t>=1):
            metals[t]=metalc
            metals[t-1]=metal
            t-=1
            metalc=metals[t-1]
            valuec=metalc.valuePerBar
            metal=metals[t]
            curValue=metal.valuePerBar

def sortMetalsByValuePerWeight(metals):
    """
    Sort the metals by value per weight using insertion sort.  The list of
    metals is modified in place to be ordered by value per weight.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """
    for i in range (1, len(metals)):
        t=i
        metalp=metals[t-1]
        valuep=metalp.valuePerWeight
        metal=metals[t]
        curValue=metal.valuePerWeight
        while(curValue>valuep and t>=1):
            metals[t]=metalp
            metals[t-1]=metal
            t-=1
            metalp=metals[t-1]
            valuep=metalp.valuePerWeight
            metal=metals[t]
            curValue=metal.valuePerWeight


def printMetals(metals):
    """
    Display the metals to standard output.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """
    for i in range (len(metals)):
        metal = metals[i]
        print("Metal( name:", metal.name, ", totalBars:", metal.totalBars, "weightPerBar:", metal.weightPerBar, ",valuePerBar:", metal.valuePerBar, ", valuePerWeight:", metal.valuePerWeight, ", bars taken:", metal.barsTaken, ")")

def main():
    """
    Runs functions
    """
    metals = readMetals("data.txt")
    printMetals(metals)
    print("Sorted by valuePerWeight:")
    sortMetalsByValuePerWeight(metals)
    printMetals(metals)
    print("Sorted by valuePerBar:")
    sortMetalsByValuePerBar(metals)
    printMetals(metals)

main()