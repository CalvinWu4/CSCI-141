"""
Author: Calvin Wu
Author: ben k steele <bks@cs.rit.edu>
Author: sean strout <sps@cs.rit.edu>
"""

from rit_lib import *

class linkedNode(struct):
    _slots=(((object,'data'),(int,'timesLanded'),(NoneType,'linkedNode'),'next'))

class linkedList(struct):
    _slots=(((linkedNode,NoneType),'head'),(int,'size'), ((linkedNode,NoneType),'cursor'))

def newNode(element):
    """
    Creates a linkedNode with element for object, 0 for timesLanded, and None for linkedNode
    :param element: object you want to add
    :return:linked Node
    """
    node=linkedNode(element,0,None)
    return node

def forward(lst):
    """
    Moves the cursor forward.
    :preconditions: 0<=cursor<=lst.size
    :param lst: The list to move its cursor forward
    :return: None
    """
    lst.cursor=lst.cursor.next

def add(lst,element):
    """
    :preconditions: None
    :param lst: The list to add the element to
    :param element: String
    :return: List with element added
    """
    if lst.head==None:
        lst.head=newNode(element)
    else:
        lst.cursor=lst.head
        while hasNext(lst):
            lst.cursor=lst.cursor.next
        lst.cursor.next=newNode(element)
        lst.size+=1

def hasNext(lst):
    """
    Returns True if the list has more elements.

    Parameters:
        lst (SlList) - the linked list
    Returns:
        True (bool) if the cursor is value
    """

    return not lst.cursor == None

def reset(lst):
    """
    Resets the cursor to the start of the list

    Parameters:
        lst (SlList) - the linked list
    Returns:
        None
    """
    lst.cursor=lst.head

