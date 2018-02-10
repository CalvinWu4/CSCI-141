"""
file: wordData.py
description: This is a supporting module which includes class definitions and utility functions relevant to all tasks
language: python3
author: Calvin Wu, cwx7054@rit.edu
date: 12/04/2015
"""

from rit_lib import *

class YearCount(struct):
    _slots=((int,'year'),(int,'count'))

class WordTrend(struct):
    _slots=((str,'word'),(float,'trend'))

def readWordFile(fileName):
    """
    Creates a dictionary mapping words to lists of YearCount objects given the name of a unigram data file
    :param fileName: text file
    :return: dict
    """
    wordDict={}
    wordList=[]
    file=open('data/'+fileName)
    for line in file:
        line=line.strip()
        if line[0].isalpha():
            currWord=line
            toggle=False
            wordList=[]
        else:
            if toggle==True:
                wordList.append(YearCount(int(line[:4]),int(line[5:])))
            if toggle==False:
                wordList.append(YearCount(int(line[:4]),int(line[5:])))
                wordDict[currWord]=wordList
                toggle=True

    return wordDict

def totalOccurrences(word,words):
    """
    Returns the total occurrences that a word has appeared in print given a dictionary
    :param word: str
    :param words: dict
    :return: int
    """
    total=0
    for i in words[word]:
        total+=i.count
    return 'Total occurrences of ' + word + ': ' + str(total)

if __name__ == '__main__':
    words=readWordFile(input('Enter word file: '))
    print(totalOccurrences((input('Enter word: ')),words))