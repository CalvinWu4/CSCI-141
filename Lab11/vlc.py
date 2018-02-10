"""
file: vlc.py
description: main program to generate variable length code output
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 11/23/2015
"""

from rit_lib import *
from array_heap import *
from math import *

class symbol(struct):
    _slots = ((str,'name'),(int,'freq'),(str,'codeword'))

class node(struct):
    _slots=((int,'totalFreq'),(list,'objects'))

def compareFunc(node1,node2):
    """
    Returns if node1 is less than node 2 for heap function
    :param node1: node
    :param node2: node
    :return: bool
    """
    return node1.totalFreq<node2.totalFreq

def read(file):
    """
    Puts the symbol and frequency for the letters from a text file into a node, calculates the codewords for each, and returns a node with all the letters and their codewords
    :param file: text file
    :return: node
    """
    symbols=''
    for i in file:
        symbols+=i
    symbols=symbols.strip()
    symbolsdict={}
    for i in symbols:
        symbolsdict[i]=0
    for i in symbols:
        symbolsdict[i]+=1
    x=symbolsdict.keys()
    y=symbolsdict.values()
    keyslist=[]
    valueslist=[]
    symbolslist=[]
    nodeslist=[]
    newnodeslist=[]
    for i in x:
        keyslist.append(i)
    for i in y:
        valueslist.append(i)
    for i in range(len(keyslist)):
        symbolslist.append(symbol(keyslist[i],valueslist[i],''))
    for i in range(len(symbolslist)):
        nodeslist.append(node(symbolslist[i].freq,[symbolslist[i]]))
    heap=createEmptyHeap(1,compareFunc)
    for i in range(len(nodeslist)):
        add(heap,nodeslist[i])
    while heap.size>1:
        newnodeslist.append(removeMin(heap))
        newnodeslist.append(removeMin(heap))
        for i in newnodeslist[0].objects:
            i.codeword='0'+i.codeword
        for i in newnodeslist[1].objects:
            i.codeword='1'+i.codeword
        newnode=node(newnodeslist[0].totalFreq+newnodeslist[1].totalFreq,newnodeslist[0].objects+newnodeslist[1].objects)
        add(heap,newnode)
        newnodeslist=[]
    return removeMin(heap)

def output(node):
    """
    Prints out variable code output for each letter, the average VLC codeword length, and the average fixed length codeword length
    :param node: node
    :return:  NoneType
    """
    print('')
    print('Variable Length Code Output')
    print('--------------------------------------------------')
    for i in node.objects:
        print('Symbol: %2s  ' % i.name, end='')
        print('Codeword: %8s  ' %i.codeword, end='')
        print('Frequency: %5s  ' %i.freq)
    average=0
    denom=0
    for i in node.objects:
        average+=(len(i.codeword)*float(i.freq))
        denom += float(i.freq)
    average=average/denom
    print('')
    print('Average VLC codeword length: ' + str(average) + ' bits per symbol')
    print('Average Fixed length codeword length: ' + str(log(len(node.objects),2)) + ' bits per symbol')

if __name__ == '__main__':
    output(read(open(input('Please enter symbol filename: '))))
