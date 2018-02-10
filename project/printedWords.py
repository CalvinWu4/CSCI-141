"""
file: printedWords.py
description: This is a program which can compute the total number of printed words for each year.
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 12/04/2015
"""

from rit_lib import *
from wordData import *
from simplePlot import *

YearList=[]
def YearListMaker(words):
    for i in words:
        for j in words[i]:
            if j.year not in YearList:
                YearList.append(j.year)
    return(sorted(YearList))

def printedWords(words):
    """
    Returns a list containing a YearCount entry for each year for which data exists given a dictionary mapping
    words to lists of YearCount objects
    :param words: dict
    :return: list
    """
    lst=YearListMaker(words)
    newLst=[]
    c=0
    while c<len(lst):
        for i in words:
            for j in words[i]:
                if j.year==lst[c]:
                    newLst.append(j)
        c+=1
    return newLst

def wordsForYear(year,yearList):
    """
    Returns an integer count representing the total # of printed words for that year
    given an integer for the year and a list of YearCount objects
    :param year: int
    :param yearList: list
    :return:
    """
    total=0
    for i in yearList:
        if i.year==year:
           total+=i.count
    return total
if __name__ == '__main__':
    yearList=input('Enter a file name: ')
    year=input('Enter year: ')
    print('Total printed words in ' + str(year) +': ' + str(wordsForYear((int(year)),printedWords(readWordFile(yearList)))))
    wordsForYearList=printedWords(readWordFile(yearList))
    print(wordsForYearList)
    labels='Year', 'Total Words'
    plot=plot2D('Number of printed words over time', labels)
    for yc in wordsForYearList:
        point=yc.year,yc.count
        plot.addPoint(point)
    plot.display()