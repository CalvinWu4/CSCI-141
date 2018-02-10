"""
Calvin Wu
"""

from rit_lib import *

class Num(struct):
    _slots=(int,'value')

class Mul(struct):
    _slots=()

class Add(struct):
    _slots=()

class BinOp(struct):
    _slots=(((Num, 'BinOp'),'left'),((Add,Mul),'op'),((Num,'BinOp'),'right'))

def createProd(a,b):
    """
    Creates an expression tree with a and b as the values for left and right respectively and Mul as the op.
    :param a: int
    :param b: int
    :return: BinOp
    """
    return (BinOp(a,Mul(),b))

def createSum(a,b):
    """
    Creates an expression tree with and b as the values for left and right respectively and Add as the op.
    :param a: int
    :param b: int
    :return: BinOp
    """
    return (BinOp(a,Add(),b))

def interp(tree):
    """
    Takes one argument, an expression tree, and returns a number, the value that the tree denotes.
    :param tree: BinOp
    :return: int
    """
    if type(tree)==Num:
        return tree.value
    elif type(tree)==BinOp:
        if tree.op == Mul():
            return interp(tree.left) * interp(tree.right)
        elif tree.op == Add():
            return interp(tree.left) + interp(tree.right)
        else:
            return ValueError("Only Add and Mul operators allowed")
    else:
        raise TypeError("The tree is the wrong type")

def expToString(tree):
    """
    One argument, an expression tree, and returns a string, which is the fully parenthesized representation of the
    tree
    :param tree: BinOp
    :return: string
    """
    string=''
    if type(tree)==Num:
        string += str(tree.value)
    elif type(tree)==BinOp:
        if tree.op == Mul():
            string += '(' + expToString(tree.left) + '*' + expToString(tree.right) + ')'
        elif tree.op == Add():
            string += '(' + expToString(tree.left) + '+' + expToString(tree.right) + ')'
        else:
            ValueError("Only Add and Mul operators allowed")
    else:
        TypeError("The tree is the wrong type")
    return string

def test_interp():
    """
    Tests the operations of interp
    :return: bool
    """
    if interp(createSum(Num(1),Num(1)))== 2:
        print(True)
    else:
        print(False)
    if interp(createSum(Num(0),Num(-2))) == -2:
        print(True)
    else:
        print(False)
    if interp(createProd(Num(3),Num(3)))==9:
        print(True)
    else:
        print(False)
    if interp(createProd(Num(-5),Num(-3)))==15:
        print(True)
    else:
        print(False)
    if interp(createSum(Num(2),createProd(Num(3),Num(4)))) == 14:
        print(True)
    else:
        print(False)
    if interp(createSum(Num(223),(createProd(Num(7),createSum(Num(105),Num(6))))))== 1000:
        print(True)
    else:
        print(False)

def test_expToString():
    """
    Tests the operations of expToString
    :return: bool
    """
    if expToString(createSum(Num(1),Num(1)))== '(1+1)':
        print(True)
    else:
        print(False)
    if expToString(createSum(Num(0),Num(-2))) == '(0+-2)':
        print(True)
    else:
        print(False)
    if expToString(createProd(Num(3),Num(3)))=='(3*3)':
        print(True)
    else:
        print(False)
    if expToString(createProd(Num(-5),Num(-3)))=='(-5*-3)':
        print(True)
    else:
        print(False)
    if expToString(createSum(Num(2),createProd(Num(3),Num(4)))) == '(2+(3*4))':
        print(True)
    else:
        print(False)
    if expToString(createSum(Num(223),(createProd(Num(7),createSum(Num(105),Num(6))))))== '(223+(7*(105+6)))':
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    test_interp()
    test_expToString()

