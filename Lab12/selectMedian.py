"""
file: selectMedian.py
description: a program that computes the median using the quick-select algorithm
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 12/08/2015
"""

from rit_lib import *
from time import *

startTime=clock()

def select(L,i):
    """
    Sorts a given list and then returns the number at a given index
    :param L: number list
    :param i: desired index
    :return: int at i
    """
    if L==[]:
        raise IndexError('Bad index')
    x=len(L)//2-1
    pivot=L[x]
    less=[]
    same=[]
    more=[]
    for num in L:
        if num<pivot:
            less.append(num)
        if num==pivot:
            same.append(num)
        if num>pivot:
            more.append(num)
    if i<len(less):
        return select(less,i)
    elif i<(len(less)+len(same)):
        return pivot
    else:
        return select(more,i-((len(less))+(len(same))))

if __name__=="__main__":
    lst=[]
    file=open(input('Enter file name: '))
    for line in file:
        line=line.strip()
        lst.append(int(line))
    if len(lst)%2==1:
        print(select(lst,(len(lst)//2)-1))
    else:
        print(((select(lst,len(lst)//2))+(select(lst,(len(lst)//2)-1)))/2)

print('Takes', clock()-startTime, 'seconds to run program')
