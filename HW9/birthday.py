"""
Calvin Wu
"""

from rit_lib import *
from random import *

def birthday():
    """
    Figures out how many people on average need to be in a room for two of them to share a birthday.
    :return: int
    """
    mySet=set()
    testsinit=int(input('Number of test (10-10000):'))
    tests=0
    adds=0
    result=0
    dupfound=False
    if testsinit<=10000 and testsinit>=10:
        while tests!=testsinit:
            while dupfound==False:
                date=randint(1,364)
                if date not in mySet:
                    mySet.add(date)
                    adds+=1
                else:
                    adds+=1
                    result+=adds
                    dupfound=True
            else:
                tests+=1
                dupfound=False
                adds=0
                mySet=set()
        else:
            print(round(result/testsinit))
    else:
        print('Incorrect value for tests')

def main():
    """
    Executes birthday function
    :return: int
    """
    birthday()

main()