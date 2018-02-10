"""
Calvin Wu
"""

"""
test_debug_hw.py homework for csci141.
"""
import pdb
#######################################################################
## problem 1 of 3.
#######################################################################
# There is a problem with the create_multiplication_table function below.
# Assignment 1:
# 1.1. Develop a suite of tests to properly test the function.
#      Due to the nature of this function they will have to be manually
#      or visually verified.
# 1.2. Debug this faulty function to locate and correct the problem.
# A screen shot of your debugger when you find at least one error
#      is required.

def create_multiplication_table(size):
    """
	create_multiplication_table: Size -> None
	create_multiplication_table creates a multiplication table.
	preconditions: size is an integer

	example: create_multiplication_table(3) should yield
	     0   1   2   3
        ==============
     0:  0   0   0   0
     1:  0   1   2   3
     2:  0   2   4   6
     3:  0   3   6   9
	"""
    j = 0
    header = "    "
    while (j <= size):
        header = header + j.__str__()
        header = header + "   "
        j = j + 1
    print(header)
    j = 0
    divider = ""
    while(j < len(header)):
        divider = divider + "="
        j = j + 1
    print(divider)
    create_rows(size, size)

def create_rows( size, row ):
    if(row < 0):
        pass
    else:
        create_rows(size, row - 1)
        print_row(size, row)

def print_row(size, row):
    row_str = row.__str__() + ":  "
    j = 0
    while(j <= size):
        row_str = row_str + calculate_value(j, row)
        row_str = row_str + "   "
        j = j + 1
    print(row_str)

def calculate_value(x, y):
    if x == 0:
        return "0"
    elif y == 0:
        return "0"
    else:
        j = 0
        value = 1
        while(j < x):
            value = x * y
            j = j + 1
        return value.__str__()

def test_create_multiplication_table():
    """
    a suite of test cases to validate that create_multiplication_table works.
    """
    # Complete this test function.
    create_multiplication_table(0)
    create_multiplication_table(1)
    create_multiplication_table(-1)
    create_multiplication_table(3)

#######################################################################
## problem 2 of 3.
#######################################################################
# There is a problem with the is_palindrome function below.
# Assignment 2:
# 2.1. Develop a suite of tests to properly test the function.
# 2.2. Debug this faulty function to locate and correct the problem.
#      A screen shot of your debugger when you find atleast one error
#      is required.

def is_palindrome(st1):
    """
    is_palindrome : String String -> Boolean
    is_palindrome tells if a string is a palindrome.
   A palindrome is a string that is the same forward and backward.
    preconditions: st1 is character string.
    """
    i = 0
    j = len(st1)-1
    while j > 0:
        if st1[i] != st1[j]:
            print("false")
            return False
        i += 1
        j -= 1
    print("true")
    return True

def test_is_palindrome():
    """
    a suite of pass/fail test cases to validate that is_palindrome works.
    """
    # Complete this test function.
    is_palindrome("a")
    is_palindrome("hello")
    is_palindrome("")
    is_palindrome("racecar")

# DO NOT CALL YOUR TEST FUNCTIONS HERE. See end of this file for directions.

#######################################################################
## problem 3 of 3.
#######################################################################
# There is a problem with the str_search function below.
# Assignment 3:
# 3.1. Develop a suite of tests to properly test this function.
# 3.2. Debug this faulty function to find and fix the problems.
#      The function is called indirectly by main_search.
#      You can use your test suite and/or main_search for debugging.
#      Initial Hints: search for J, L, or C.
# 3.3. Document your debugging results trying to fix the str_search code.
#      A screen shot of your debugger when you find atleast one error
#      is required.

def str_search(data, target, start, end):
    """
    str_search : String String NatNum NatNum -> NatNum or NoneType
    Description:
    Search for a target value in a sorted data string.
    The search happens between the start and end indices inclusively.
    This starts searching in the middle. If it finds the target, it is done.
    Otherwise it decides whether to search the first half or the second half.
    preconditions: the data string is in ascending alphanumeric order.
    Parameters:
        data - a string
        target - the target value to find is a single character string e.g. 'Q'
        start - the starting index into the data
        end - the ending index into the data
    Returns:
        index of target in data, if present; otherwise None.
    """

    if start > end:
        return None

    mid_index = ( start + end ) // 2
    mid_value = data[mid_index]

    # debug statement prints the data.
    #print( "Searching for", target, ":", data[start:mid_index],
    #    "*" + str( mid_value ) + "*", data[mid_index+1:end+1] )

    if target == mid_value:
        return mid_index
    elif target < mid_value:
        return str_search(data, target, start, mid_index - 1)
    else:
        return str_search(data, target, mid_index + 1, end)


def find_target(data, target):
    """
    find_target : String String -> NatNum or NoneType
    find_target returns the index of target in data or None if not found.
    Parameters:
        data - a string
        target - the target value to find
    Returns:
        The index of the target element in data, if present, or None.
    """

    return str_search(data, target, 0, len(data) - 1)


def makeString():
    """
    makeString : () -> String
    makeString returns a String
    """
    data = ""
    # append characters to make the string
    for num in range(36, 108, 2):
        data += chr(num)
    return data


def main_search():
    """
    main_search : Void -> NoneType
    """

    data = makeString()
    print("Number of elements: ", len(data))

    while True:
        print("\nData: ", data)
        target = input("Enter a character to find: ")

        if target == "":
            break
        else:
            index = find_target(data, target)
            print()
            if index != None:
                print(target, "found at index", index)
            else:
                print(target, "not found")
                # end while


def test_str_search():
    """
    a suite of pass/fail test cases to validate that str_search works.
    """
    # Complete this test function.
    print(str_search(makeString(), 'j', 0, 35))
    print(str_search(makeString(), 'l', 0, 35))
    print(str_search(makeString(), 'c', 0, 35))
    print(str_search(makeString(), '', 0, 35))
    print(str_search(makeString(), '$', 0, 35))
    print(str_search(makeString(), 'P', 0, 35))

#######################################################################
# 3.3. Document your debugging results trying to fix the str_search code.
# Enter answers to the questions below inside the triple-quoted string.
"""
	Were you able to completely fix str_search? Yes
	If not, explain in detail the cases that still fail.
	What tool(s) did you use? Debugger
	What went well? Seeing the recursion error and how the variable values changed
	What problems did you have? Finding how to affect the variable values
"""
#######################################################################

if __name__ == "__main__":
    #
    # Run the test functions for problem 1, problem 2, and problem 3.
    #
    #test_is_reverse_of()
    #test_str_search()
    #
    #main_search()
    test_create_multiplication_table()
    test_is_palindrome()
    test_str_search()

# After finishing the problems, submit this file to the mycourses dropbox.