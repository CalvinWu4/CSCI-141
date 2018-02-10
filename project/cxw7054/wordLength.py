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
    # sortedLst=sortedLst[:((len(sortedLst))//2)]
    # dict={}
    # for i in sortedLst:
    #     dict[i[0]]=i[1]
    #Constructing a sorted list of items sorted by word length from given dictionary
    total=0
    dict={}
    for i in words:
        for j in words[i]:
            if j.year==year:
                dict[i]=len(i),j.count
                total+=j.count
    sortedLst=dict.items()
    counter=0
    sortedLst=sorted(sortedLst,key=lambda sortedLst:sortedLst[1][0])
    #Computing the min and max
    min=sortedLst[0][1][0]
    max=sortedLst[-1][1][0]
    #Computing the median
    medTotal=total/2
    index=0
    while total>medTotal:
        for i in sortedLst:
            while counter<i[1][1] and total>medTotal:
                counter+=1
                total-=1
                if counter==i[1][1]:
                    index+=1
            counter=0
    med=sortedLst[index][1][0]
    median=sortedLst[index]
    #Computing the first quartile
    q1Lst=[]
    i=0
    while sortedLst[i]!=median:
        q1Lst.append(sortedLst[i])
        i+=1
    index=0
    counter=0
    medTotal=total/2
    while total>medTotal:
        for i in q1Lst:
            while counter<i[1][1] and total>medTotal:
                counter+=1
                total-=1
                if counter==i[1][1]:
                    index+=1
            counter=0
    q1=q1Lst[index][1][0]
    #Computing the third quartile
    q3Lst=[]
    i=0
    sortedLst=sortedLst[::-1]
    while sortedLst[i]!=median:
        q3Lst.append(sortedLst[i])
        i+=1
    index=0
    counter=0
    total=total*2
    medTotal=total/2
    while total>medTotal:
        for i in q3Lst:
            while counter<i[1][1] and total>medTotal:
                counter+=1
                total-=1
                if counter==i[1][1]:
                    index+=1
            counter=0
    q3=q3Lst[index][1][0]
    print('minimum: '+ str(min))
    print('1st quartile: '+str(q1))
    print('median: '+str(med))
    print('3rd quartile: '+str(q3))
    print('maximum: '+str(max))
    boxAndWhisker(min,q1,med,q3,max)
    return(min,q1,med,q3,max)

if __name__ == '__main__':
    words=input('Enter word file: ')
    year=int(input('Enter year: '))
    summaryFromWords((readWordFile(words)),year)