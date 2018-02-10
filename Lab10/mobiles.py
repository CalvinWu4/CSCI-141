"""
file: mobiles.py
language: python3
author: ben k steele, bks@cs.rit.edu
author: Calvin Wu cxw7054
description: Build mobiles using a tree data structure.
date: 11/2015
purpose: starter code for the tree mobiles lab
"""

from rit_lib import *

############################################################
# structure definitions
############################################################

class Ball(struct):
    """
    class Ball represents a ball of some weight hanging from a cord.
    field description:
    cord: length of the hanging cord in inches
    weight: weight of the ball in ounces (diameter of ball in a drawing)
    """

    _slots = ((float,'cord'),(float,'weight'))

class Rod(struct):
    """
    class Rod represents a horizontal rod part of a mobile with
    a left-side mobile on the end of a left arm of some length,
    and a right-side mobile on the end of a right arm of some length.
    In the middle between the two arms is a cord of some length
    from which the rod instance hangs.
    field description:
    leftmobile: subordinate mobile is a mobile type.
    leftarm: length of the right arm in inches
    cord: length of the hanging cord in inches
    rightarm: length of the right arm in inches
    rightmobile: subordinate mobile is a mobile type.

    An assembled mobile has valid left and right subordinate mobiles;
    an unassembled mobile does not have valid subordinate mobiles.
    """

    _slots = (((Ball,'Rod',str),'leftmobile'),(float,'leftarm'),(float,'cord'),(float,'rightarm'),((Ball,'Rod',str),'rightmobile'))

#########################################################
# Create mobiles from mobile files
#########################################################

def readMobile( file ):
    """
    readMobile : OpenFileObject -> Map( Ball | Rod )
    readMobile reads the open file's content and
    builds a mobile 'parts map' from the specification in the file.
    The parts map returned has components for assembling the mobile.
    If the mobile is a simple mobile, the returned value is
    a parts map containing a Ball instance.
    If the mobile is complex, the returned value is a parts list of
    the Rod instance representing the top-most mobile component and
    the other parts.
    The connection point for each part is a string that identifies
    the key name of the part to be attached at that point.

    If there is an error in the mobile specification, then
    return an empty parts map.

    # an example of the file format. 'B10' is key for the 10 oz ball.
    # blank lines and '#' comment lines are permitted.
    B10 40 10

    top B10 240 66 80 B30
    B30 55 30
    """

    partsmap={}
    for line in file:
        line=line.strip()
        if len(line)==0:
            pass
        else:
            if line[0]=='#':
                print(line)
            else:
                lst=line.split()
                if len(lst)==3:
                    partsmap[lst[0]]=Ball(float(lst[1]),float(lst[2]))
                elif len(lst)==6:
                    partsmap[lst[0]]=Rod(lst[1],float(lst[2]),float(lst[3]),float(lst[4]),lst[5])
    return partsmap

def constructMobile( partsmap ) :
    """
    constructMobile : Map( Rod | Ball ) -> Ball | Rod | NoneType

    constructMobile reads the partsmap to put together the
    mobile's components and return a completed mobile object.
    The constructMobile operation 'patches entries' in the partsmap.

    The parts map has the components for assembling the mobile.
    Each Rod in partsmap has a key name of its left and right
    subordinate mobiles.  constructMobile reads the key to
    get the subordinate part and attach it at the slot where
    the key was located within the component.

    The top mounting point of the mobile has key 'top' in partsmap.

    If the completed mobile object is a simple mobile, then
    the top returned value is a Ball instance.
    If the completed mobile is a complex mobile, then
    the top returned value is a Rod instance.

    If the parts map contains no recognizable mobile specification,
    or there is an error in the mobile specification, then 
    return None.
    """

    for i in partsmap.values():
        if isinstance(i,Rod):
            if isinstance(i.leftmobile,str):
                i.leftmobile=partsmap[i.leftmobile]
            if isinstance(i.rightmobile,str):
                i.rightmobile=partsmap[i.rightmobile]
    return partsmap['top']

############################################################
# mobile analysis functions
############################################################

def is_balanced( theMobile ) :
    """
    is_balanced : theMobile -> Boolean

    is_balanced is trivially True if theMobile is a simple ball. 

    Otherwise theMobile is balanced if the product of the left side
    arm length and the left side is approximately equal to the 
    product of the right side arm length and the right side, AND
    both the right and left subordinate mobiles are also balanced.

    The approximation of balance is measured by checking
    that the absolute value of the difference between
    the two products is less than 1.0.

    If theMobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: theMobile is a proper mobile instance.
    """
    if isinstance(theMobile,Ball):
        return True
    if isinstance(theMobile,Rod):
        lefttotal = weight(theMobile.leftmobile)*theMobile.leftarm
        righttotal = weight(theMobile.rightmobile)*theMobile.rightarm
        if abs(lefttotal-righttotal)<1:
            return True
        else:
            return False
    else:
        raise Exception( "Error: Not a valid mobile\n\t" + str( theMobile ) )

def weight( theMobile ) :
    """
    weight : theMobile -> Number
    weight of the theMobile is the total weight of all its Balls.

    If theMobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: theMobile is a proper mobile instance.
    """
    if isinstance(theMobile,Ball):
        return theMobile.weight
    if isinstance(theMobile,Rod):
        total = weight(theMobile.leftmobile)+weight(theMobile.rightmobile)
        return total
    else:
        raise Exception( "Error: Not a valid mobile\n\t" + str( theMobile ) )
 
def height( theMobile ) :
    """
    height : theMobile -> Number
    height of the theMobile is the height of all tallest side.

    If theMobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: theMobile is a proper mobile instance.
    """
    if isinstance(theMobile,Ball):
        return theMobile.cord + theMobile.weight
    if isinstance(theMobile,Rod):
        lefttotal=height(theMobile.leftmobile)
        righttotal=height(theMobile.rightmobile)
    else:
        raise Exception( "Error: Not a valid mobile\n\t" + str( theMobile ) )
    if lefttotal>righttotal:
        return lefttotal+theMobile.cord
    else:
        return righttotal+theMobile.cord

def width( theMobile ) :
    """
    width : theMobile -> Number
    return the rotational diameter width of the theMobile.

    The width of its widest point must take into account 
    the rotation of complex mobiles.

    If theMobile is a Rod with submobiles, then
    the width has special issues because the mobile may spin.
    The possible spin rotation may cause the widest side
    to shift from one side of the hanging point to another.

    To account for this spinning, this function needs help to
    calculate the width of the widest single side.
    Then it takes the widest side width and 
    doubles the widest side to use as the width of whole mobile.

    If theMobile is a only simple Ball,
    then the width of the 'widest side' of the ball is the radius,
    and doubling the radius is the width of the whole mobile.
    (Remember that the ball's weight also represents its diameter.)
    """
    if isinstance(theMobile,Ball):
        return theMobile.weight
    if isinstance(theMobile,Rod):
        lefttotal=(theMobile.leftarm)
    if isinstance(theMobile,Rod):
        righttotal=(theMobile.rightarm)
    else:
        raise Exception( "Error: Not a valid mobile\n\t" + str( theMobile ) )
    if lefttotal>righttotal:
        return lefttotal*2
    else:
        return righttotal*2

def main():
    """
    Prompts for file name, constructs a mobile, prints mobile analysis functions, and prompts for enter key to close
    :return: NoneType
    """
    f=(input('Enter a mobile file name'))
    x=readMobile(open(f))
    y=constructMobile(x)
    print('file: ' + str(f))
    print('isbalanced?: ' + str(is_balanced(y)))
    print('weight: ' + str(weight(y)))
    print('height: ' + str(height(y)))
    print('width: ' + str(width(y)))
    input('Hit enter to close')
main()
