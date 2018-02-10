"""Calvin Wu"""

from turtle import *

####################################################################
# The "tt" names are a specified public interface.
# STUDENT: complete the definitions for the stubbed functions.
####################################################################

def ttEvaluateReverse(program):
    """
    helper function for bang symbol to evaluate program in reverse
    """
    for i in program:
        if i.isdigit() == True:
            if int(i) >= 0 and int(i) <= 9:
                program.replace(i,'RR' + i)
        elif i is '<':
            program.replace('<','>')
        elif i is 'L':
            program.replace('L','R')
        elif i is '>':
            program.replace('>','<')
        elif i is 'R':
            program.replace('R','L')
        elif i is ' ':
            pass
    return program

def ttEvaluateMirror(string):
    '''
    helper function for @ symbol to reflect drawing
    '''
    mirror=ttEvaluateReverse(string)
    for i in range(0,len(string)):
        char=string[i]
        if char == '<':
            mirror=mirror+'>'
        elif char=='>':
            mirror=mirror+'<'
        elif char=='L':
            mirror=mirror+'R'
        elif char=='R':
            mirror=mirror+'L'
        else:
            mirror=mirror+char
    return mirror
    """
    evaluate program as a TinyTurtle language program.
    program -- a TinyTurtle string.
    precondition: program contains only TinyTurtle drawing commands.
    """
def ttEvaluate(program):
    for i in program:
        if program[:len(program) == '!']:
            program
        elif i.isdigit() == True:
            if int(i) >= 0 and int(i) <= 9:
                forward(int(i)*10)
        elif i is '<':
            left(15)
        elif i is 'L':
            left(90)
        elif i is '>':
            right(15)
        elif i is 'R':
            right(90)
        elif i is ' ':
            pass
        else:
            print("Error")
            return
    return

def ttInterpret( program ):
    """
    interpret program as a TinyTurtle language string.
    program -- a TinyTurtle string, possibly with string manipulation symbols
    """
    # REMOVE THIS LINE AND THE print STATEMENT WHEN YOU IMPLEMENT THIS FUNCTION.

    return

def ttExpand(program) :
    """
    expand the string manipulation symbols in program into
    a TinyTurtle language program.
    program -- a TinyTurtle string, possibly with string manipulation symbols
    Returns -- a TinyTurtle string after expansion
    """
    string=''
    atsymbol=0
    stringatsymbol=0
    for i in range(0,len(program)):
        char=program[i]
        if char == '@':
            atsymbol=char
            stringatsymbol=len(string)-1
        elif char=='/':
            string=string+string[stringatsymbol:]
        elif char=='!':
            string=string+ttEvaluateReverse(string[stringatsymbol:])
        elif char=='':
            string=string+ttEvaluateMirror(string[stringatsymbol:])
        else:
            string=string+char
        print(string)
        return string