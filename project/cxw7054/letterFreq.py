"""
file: letterFreq.py
description: This is a program which can compute the relative frequency of English characters occurring in print.
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 12/04/2015
"""

from rit_lib import *
from wordData import *

def combineValues(words):
    """
    Helper function for letterFreq
    Returns a dict of words mapping their total occurrences in print given a dictionary
    mapping words to lists of YearCount objects
    :param words: dict
    :return: dict
    """
    keys=(list(words.keys()))
    y=0
    countDict={}
    for i in words.values():
        z=keys[y]
        total=0
        if y<len(keys):
            y+=1

        for j in i:
            if z in countDict:
                total+=j.count
                countDict.update({z:(total)})
            else:
                total+=j.count
            countDict[z]=total
    return(countDict)

def letterFreq(words):
    """
    Returns the total occurrences that a word has appeared in print given a dictionary
    :param words: dict
    :return: int
    """
    letterDict = {}
    valuesList=[]
    newDict=(combineValues(words))
    for word in list(words.keys()):
        occurrences=newDict[word]
        for letter in word:
            letterDict[letter] = letterDict.get(letter, 0) + occurrences
    letter_items = list(letterDict.items())
    letter_items.sort()
    for i in letter_items:
        valuesList.append((i[1]))
    valuesList.sort()
    valuesList=valuesList[::-1]
    newList=valuesList.copy()
    c=0
    toggle=False
    for i in letter_items:
        letterValue=i[1]
        toggle=False
        for j in range(len(letter_items)):
            if newList[j]==letterValue and isinstance(newList[j],int) and toggle==False:
                toggle=True
                newList[j]=i
        if valuesList[c]==letterValue:
             newList[c]=i
             c+=1
    newString=''
    for i in newList:
        newString+=i[0][0]
    return newString

if __name__ == '__main__':
    print(letterFreq(readWordFile(input('Enter file name: '))))