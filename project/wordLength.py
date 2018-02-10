"""
file: wordLength.py
description: This is a program which can compute the distribution of word lengths
and the five number summary of those word lengths.
trending words between a given starting and ending year.
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 12/04/2015
"""

from turtle import *
from rit_lib import *
from wordData import *
from boxAndWhisker import *

def summaryFromWords(words,year):
    """
    Returns a five-tuple containing five numbers representing the five number summary given a dictionary mapping words
    to lists of YearCount objects and a natural number representing the year of interest.
    :param words: dict
    :param year: int
    :return: tuple
    """
    total=0
    dict={}
    for i in words:
        for j in words[i]:
            if j.year==year:
                dict[i]=len(i),j.count
                total+=j.count
        sortedLst=dict.items()
    sortedLst=sorted(sortedLst,key=lambda sortedLst:sortedLst[1][1])
    sortedLst=sorted(sortedLst,key=lambda sortedLst:sortedLst[1][0])
    return sortedLst

def summaryFromWords1(words,year):
    """
    Returns a five-tuple containing five numbers representing the five number summary given a dictionary mapping words
    to lists of YearCount objects and a natural number representing the year of interest.
    :param words: dict
    :param year: int
    :return: tuple
    """
    total=0
    dict={}
    for i in words:
        for j in words[i]:
            if j.year==year:
                dict[i]=len(i),j.count
                total+=j.count
        sortedLst=dict.items()
    sortedLst=sorted(sortedLst,key=lambda sortedLst:sortedLst[1][1])
    sortedLst=sorted(sortedLst,key=lambda sortedLst:sortedLst[1][0])
    return total

def helper(sortedData,totalCount,float):
    target=float*totalCount
    for x in sortedData:
        if target<=x[1][1]:
            return x[1][0]
        else:
            target-=x[1][1]

def main():
    words=input('Enter word file: ')
    year=int(input('Enter year: '))
    min=(helper(summaryFromWords((readWordFile(words)),year),summaryFromWords1((readWordFile(words)),year),0))
    q1=(helper(summaryFromWords((readWordFile(words)),year),summaryFromWords1((readWordFile(words)),year),.25))
    med=(helper(summaryFromWords((readWordFile(words)),year),summaryFromWords1((readWordFile(words)),year),.5))
    q3=(helper(summaryFromWords((readWordFile(words)),year),summaryFromWords1((readWordFile(words)),year),.75))
    max=(helper(summaryFromWords((readWordFile(words)),year),summaryFromWords1((readWordFile(words)),year),1))
    boxAndWhisker(min,q1,med,q3,max)
    return(min,q1,med,q3,max)

if __name__ == '__main__':
    print(main())
