"""
file: trending.py
description: This is a program which can compute the top and bottom
trending words between a given starting and ending year.
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 12/04/2015
"""

from rit_lib import *
from wordData import *

def trending(words,startYr,endYr):
    """
    Returns a list containing a WordTrend entry for each word for which qualifying data exists given a dictionary
    mapping words to lists, an integer for the starting year, and an integer for the ending year.
    :param words: dict
    :param startYr: int
    :param endYr: int
    :return: list
    """
    startLst=[]
    endLst=[]
    WordTrendLst=[]
    lst=[]
    for i in words:
        for j in words[i]:
            if j.year==startYr:
                if j.count>=1000:
                    startLst.append(i)
    for i in startLst:
        for j in words[i]:
            if j.year==endYr:
                if j.count>=1000:
                    endLst.append(i)
    for i in endLst:
        for j in words[i]:
            if j.year==startYr:
                trendValue=j.count
            if j.year==endYr:
                trendValue=j.count/trendValue
        WordTrendLst.append(WordTrend(i,trendValue))
        trendValue=0
    return(sorted(WordTrendLst,key=lambda WordTrend:WordTrend.trend))[::-1]

if __name__ == '__main__':
    words=input('Enter word file: ')
    startYr=int(input('Enter starting year: '))
    endYr=int(input('Enter ending year: '))
    print('The top trending words from '+str(startYr)+' to '+str(endYr)+' :')
    lst=trending(readWordFile(words),startYr,endYr)
    for i in lst[:10]:
        print(i.word)
    lst=lst[::-1]
    print('')
    print('The bottom trending words from '+str(startYr)+' to '+str(endYr)+' :')
    for i in lst[:10]:
        print(i.word)