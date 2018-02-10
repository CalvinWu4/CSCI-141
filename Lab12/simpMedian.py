"""
file: simpMedian.py
description: a program that computes the median using insertion sort
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 12/08/2015
"""

from rit_lib import *
from time import *

startTime=clock()

def findMinFrom(lst,mark):
    """
    Finds the minimum number in a list given a marked index
    :param lst:  number list
    :param mark: int
    :return: int
    """
    minnum = lst[mark]
    for i in range(mark, len(lst)):
        if lst[i] < minnum:
            minnum = lst[i]
    return minnum

def swap(lst,mark,minnum):
    """
    Swaps the number at marked index with the minimum number in a number list
    :param lst: number list
    :param mark: int
    :param minnum: int
    :return: number list
    """
    pos = 0
    for i in range(mark, len(lst)):
        if lst[i] == minnum:
            pos = i
            break
    temp = lst[mark]
    lst[mark] = minnum
    lst[pos] = temp
    return lst

def selectionSort(lst):
    """
    Sorts a number list by swapping numbers into order
    :param lst: number list (unsorted)
    :return: number list (sorted)
    """
    for mark in range(0,len(lst)):
        lst = swap(lst,mark,findMinFrom(lst,mark))
    return lst

def simp(filename):
    """
    Finds the median given a file with a list of numbers by using selection sort
    :param filename: number text file
    :return: int/float
    """
    lst=[]
    file=open(filename)
    for line in file:
        line=line.strip()
        lst.append(int(line))
    selectionSort(lst)
    if lst==[]:
        return IndexError('Bad index')
    if len(lst)%2==1:
        return lst[len(lst)//2]
    else:
        return (lst[len(lst)//2]+lst[len(lst)//2-1])/2

if __name__ == '__main__':
    print(simp(input('Enter file name: ')))

print('Takes', clock()-startTime, 'seconds to run program')
