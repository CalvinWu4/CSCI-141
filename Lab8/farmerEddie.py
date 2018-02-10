"""
Calvin Wu
"""

from myList import *
from rit_lib import *
from random import random
from copy import copy

def load(filename):
    """
    Loads animals from text document into list 1 and list 2
    :preconditions: Non-empty text file
    :param filename: Text file
    :return: None
    """
    file=open(filename)
    toggle=0
    list1=linkedList((newNode(None)),0,newNode(None))
    list2=linkedList((newNode(None)),0,newNode(None))
    reset(list1)
    reset(list2)
    for x in file:
        x=x.strip()
        if x=='':
            toggle=1
            pass
        elif toggle==0:
            add(list1,x)
        else:
            add(list2,x)

def spin(currentList,timesSpin):
    """
    Spins through animals in the current list
    If the arrow lands on switch, switches animal wheel
    If the arrow lands on an animal, it increments that animal's timesLanded
    If any animal's timesLanded equals 3: it stops and declares that animal the winner
    :param currentList: List to spin through
    :param timesSpin: Number of animals it spins through before it stops
    :return: Strings (Print statements)
    """
    spinCounter=1
    winner=False
    print('Playing the game...')
    while winner == False:
        print('Spin '+ str(spinCounter) + ': ')
        while timesSpin>1:
            print(currentList.cursor.data + '->')
            forward(currentList)
            if not hasNext(currentList):
                reset(currentList)
                print(currentList.cursor.data + ' -> ')
            else:
                pass
        while timesSpin==0:
            print(currentList.cursor.data + ' -> ')
            forward(currentList)
            else:
                print(currentList.cursor.data)
            forward(currentList)
            timesSpin-=1
        spinCounter+=1
        if currentList.cursor.data=='Switch':
            print('-----Switching Wheels-----')
            if currentList==list1:
                currentList=list2
            else:
                currentList=list1
        else:
            currentList.cursor.timesLanded+=1
            list1copy=copy.copy(list1)
            list2copy=copy.copy(list2)
            reset(list1copy)
            reset(list2copy)
            while hasNext(list1copy):
                if list1copy.cursor.timesLanded==3:
                    winner=True
            while hasNext(list2copy):
                if list2copy.cursor.timesLanded==3:
                    winner=True
    else:
        print(currentList.cursor.data + 'won!')

def main():
    """
    Prompts for the input file and loads the animals into the linked list
    Prompts for the random seed
    Spins the wheel with list1 as the currentList and a random integer based on the seed
    :return: Strings (Print statements)
    """
    load(input('Enter a file for the names of the animals on the wheels'))
    spin(list1,random.randint(input('Enter a seed for the random number generator')))
main()