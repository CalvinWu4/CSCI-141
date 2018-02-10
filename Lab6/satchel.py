"""
Author: Sean Strout (sps@cs.rit.edu)
Author: ben k steele (bks@cs.rit.edu)
Author: Calvin Wu

This class represents Greedo's satchel that can store a collection
of Metal bars.  As such, it is dependent on the Metal class for its 
internal representation.  The satchel support operations for
creation, filling the entire satchel, adding a single metal bar,
and displaying the satchel.

Language: Python 3
"""
import metal
from rit_lib import *            # rit_lib class

class Satchel(struct):
    """
    Represents a satchel that can hold up to a certain weight of metals.
    :slot name (str): The name of the satchel
    :slot capacity (int): The maximum weight the satchel can hold
    :slot weight (int): The total weight of the metals in the satchel
    :slot totalValue (int): The total value of the metals in the satchel
    :slot items (list of Metal): The metals added into the satchel
    """
    _slots=((str, "name"), (int, "capacity"), (int, "weight"), (int, "totalValue"), (list, "items"))

def createSatchel(name, capacity):
    """
    Create and return a new Satchel object.
    :param name (str): The name of the satchel
    :param capacity (int): The maximum weight the satchel can hold
    :return: A newly initialized Satchel object
    :rtype: Satchel
    """
    metals=[]
    return Satchel(name, capacity, 0, 0, metals)

def fillSatchel(satchel, metals):
    """
    Fill the satchel greedily by the metal value.  This assumes the metals
    are already sorted in descending order by value (e.g. value per bar,
    or value per weight).
    :param satchel (Satchel): The Satchel object
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType

    ^^^ ^^^
    until satchel is filled or will be filled on pickup of a metal bar, add a metal to the bag,
    and edit the values of satchel accordingly
    """
    x=0
    while(x<=len(metals)-1 and satchel.capacity!=satchel.totalValue):
        metal=metals[x]
        for i in range (metal.totalBars):
            if(satchel.capacity>satchel.weight+metal.weightPerBar):
                satchel.totalValue=satchel.totalValue+metal.valuePerBar
                satchel.weight=satchel.weight+metal.weightPerBar
                addItem(satchel, metal)
        x=x+1

def addItem(satchel, metal):
    """
    Add a metal to the satchel.
    :param satchel (Satchel): The Satchel object
    :param metal (Metal): The metal to be added
    :return: None
    :rtype: NoneType
    """
    metals=satchel.items
    metals.append(metal)
    satchel.items=metals

def printSatchel(satchel):
    """
    Display the satchel to standard output in the format:
        Name: {name of satchel}
    	Capacity: {maximum weight of satchel}
    	Weight Held: {current weight of satchel}
    	Total Value: {total value of satchel}
    	Items:
    	    {first metal}
    	    {second metal}
    	    ...
    When displaying the individual metals, use the metal module function,
    printMetals().
    :param satchel (Satchel): The Satchel object
    :return: None
    :rtype: NoneType
    """
    print("Name:", satchel.name)
    print("Capacity:", satchel.capacity)
    print("Weight Held:", satchel.weight)
    print("Total Value:", satchel.totalValue)
    print("Items:")
    items=satchel.items
    for i in range (len(items)):
        print(items[i-1])
