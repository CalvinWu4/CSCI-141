"""
Calvin Wu
"""

from rit_lib import *
from myStack import *
from myNode import *

class EmptyNode(struct):
    _slots=()
class Node(struct):
    _slots=((object, 'data'),((EmptyNode,'Node'),'next'))

def moveOne(to,from2):
    element=top(from2)
    push(to,element)
    pop(from2)
    return to, from2

#lst=(can1,can2,can3)
#lst=move(1st,from2,to)

#list method
def move(lst,from2,to):
    item=top(lst[from2)])
    lst[from2]=pop(lst[from2])
    lst[to]=push(lst[to],item]])
    return lst
for i in range(0,len(lst)):
    ........

#item method
(can1,can2)=move(can1,can2)
def move(can1,can2):
    item=top(fromCan)
    fromCan=pop(fromCan)
    toCan=push(toCan,item)
    return(toCan,fromCan)
if can1
    if can2
        else can3
elif can2
    #.....
else
    #.....
