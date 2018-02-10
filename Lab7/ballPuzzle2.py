"""
Calvin Wu
"""

from rit_lib import *
from myStack import *
from myNode import *
from ballPuzzle_animate import *

lst = [EMPTY_NODE,EMPTY_NODE,EMPTY_NODE]

#(can1,can2)=move(can1,can2)
def move(fromCan,toCan):
    item=top(fromCan)
    fromCan=pop(fromCan)
    toCan=push(toCan,item)
    return(toCan,fromCan)

def solve(stackList,fromCan,toCan):
    count=0
    while size(lst[fromCan])>0:
        if top(lst[fromCan])=='G':
            move(lst[fromCan],lst[toCan])
            animate_move(lst,fromCan,toCan)
            count+=1
        else:
            toCan=2
            move(lst[fromCan],lst[toCan])
            animate_move(lst,fromCan,toCan)
            count+=1
        fromCan=2
        toCan=0
    while size(lst[fromCan])>0:
        if top(lst[fromCan])=='R':
            move(lst[fromCan],lst[toCan])
            count+=1
        else:
            move(lst[fromCan],lst[toCan])
            count+=1
        fromCan=1
        toCan=2
    while size(lst[fromCan])>0:
        if top(lst[fromCan])=='B':
            move(lst[fromCan],lst[toCan])
            count+=1
    print(count)

def main():
    x=input("Enter the initial balls in the red can")
    animate_init(x)
    for i in x:
        lst[0]=push(lst[0],i)
    solve(lst,0,1)
    input('Press enter to quit')


main()



#    while len(lst[0]) > 0:
 #       if top(lst[0]) == 'G':
  #          move(lst[0],lst[1])
   #         count+=1
    #    else:
     #       move(lst[0],lst[2])
     #       count+=1
    #while len(lst[2])>0:
      #  if top(lst[2])=='R':
       #     move(lst[2],lst[0])
        #    count+=1
       # else:
        #    move(lst[2],lst[1])
         #   count+=1
    #while len(lst[1])>0:
     #   if top(lst[1])=='B':
      #      move(lst[1],lst[2])
       #     count+=1
