"""
Calvin Wu
"""

from rit_lib import *
from slList import *
from slNode import *

def fileToList(filename):
    """
    Helper function for readFile function.
    Returns a list of the numbers in a file.
    :param filename: file
    :return: list
    """
    lst = []
    filename=open(filename)
    for line in filename:
        for element in line.split():
            lst.append(element)
    return lst

def readFile(filename):
    """
    Creates a single-linked list given a list.
    :param filename: file
    :return: linked list
    """
    lst=createList()
    for i in fileToList(filename):
        append(lst,i)
    reset(lst)
    return lst

def main():
    """
    Prints list before and after sorting
    """
    x=readFile(input("Enter the file name"))
    print(x)
    linkSort(x)
    print(x)