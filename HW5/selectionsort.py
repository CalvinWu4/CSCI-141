"""
Calvin Wu
1. Insertionsort performs better than selectionsort when there are just two numbers switched around
such as [1,5,7,12,45,24].
2. Selectionsort performs worse than insertionsort in that test case because it has to check the whole list
for the lowest numbers and and reforms the list in order whereas selectionsort just runs through the numbers and
switches numbers around if they are not in order.
"""

def findMinFrom(lst,mark):
    minnum = lst[mark]
    for i in range(mark, len(lst)):
        if lst[i] < minnum:
            minnum = lst[i]
    return minnum

def swap(lst,mark,minnum):
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
    for mark in range(0,len(lst)):
        lst = swap(lst,mark,findMinFrom(lst,mark))
    return lst

print(selectionSort([45,7,5,24,12,1]))