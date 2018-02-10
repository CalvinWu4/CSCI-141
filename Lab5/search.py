"""Calvin Wu"""

def searchChar(chr,str):
    """Searches for character in string and returns true or false"""
    if str == '':
        return False
    elif str[0] == chr:
        return True
    else:
        return searchChar(chr,str[1:])

def matchString(pre,str):
    """Searches for prefix string in string and returns true or false"""
    if pre=='':
        return True
    elif pre[0]!=str[0]:
        return False
    else:
        return matchString(pre[1:],str[1:])

def searchString(target,str):
    """Searches for target string in string and returns true or false"""
    if len(target)>len(str):
        return False
    elif target==str[:len(target)]:
        return True
    else:
        return searchString(target,str[1:])


def duplicateAsteriskRemover(str):
    """Searches for duplicate asterisks in string and removes them"""
    newList=list(str)
    while len(newList)!=1:
        if newList[0]=='*' and newList[1]=='*':
            newList.remove('*')
        else:
            break
    str = ''
    for letter in newList:
        str += letter
    return str

def matchPat(pre,str):
    """Searches for prefix pattern string in string and returns true or false"""
    if pre=='':
        return True
    pre=duplicateAsteriskRemover(pre)
    if len(pre)>len(str) and pre[0]!='*':
        return False
    elif len(pre) == 1:
        if pre[0]==str[0] or pre[0]=='*':
            return True
        else:
            return False
    elif pre[0]=='*':
        a=1
        c=0
        while c<len(str):
            if pre[a]==str[c]:
                return matchPat(pre[a:],str[c:])
            else:
                c+=1
    if pre[0]!=str[0]:
        return False
    else:
        return matchPat(pre[1:],str[1:])

def searchPat(target,str):
    """Searches for pattern string in string and returns true or false"""
    if target=='':
        return True
    if len(target)>len(str):
        return False
    target=duplicateAsteriskRemover(target)
    if len(target)>len(str) and target[0]!='*':
        return False
    elif len(target) == 1:
        if target[0]==str[0] or target[0]=='*':
            return True
        else:
            return False
    if target[0]=='*':
        a=1
        c=0
        while c<len(str):
            if target[a]==str[c]:
                return searchPat(target[a:],target[c:])
            else:
                c+=1
    else:
        return searchPat(target[1:],str[1:])

def test():
    """Tests functions"""
    """Searches for b in abc and checks to see if its true"""
    if searchChar('b','abc') == True:
        print('Pass')
    """Searches for d in abc and checks to see if its false"""
    if searchChar('d','abc') == False:
        print('Pass')
    """Searches for ab in the prefix of abc and checks to see if its true"""
    if matchString('ab','abc') == True:
        print('Pass')
    """Searches for bc in the prefix of abc and checks to see if its false"""
    if matchString('bc','abc') == False:
        print('Pass')
    """Searches for ab in abc and checks to see if its true"""
    if searchString('ab','abc') == True:
        print('Pass')
    """Searches for ac in abc and checks to see if its false"""
    if searchString('ac','abc') == False:
        print('Pass')
    """Searches for a,t, and r separated by any amount of characters in the prefix of anteater and checks to see if its true"""
    if matchPat('a*t*r','anteaters') == True:
        print('Pass')
    """Searches for a,t, and r separated by any amount of characters in the prefix of albatross and checks to see if its true"""
    if matchPat('a*t*r','albatross') == True:
        print('Pass')
    """Searches for a,t, and r separated by any amount of characters in the prefix of artist and checks to see if its false"""
    if matchPat('a*t*r','artist') == False:
        print('Pass')
    """Searches for a,t, and r separated by any amount of characters in Some anteaters are nice and checks to see if its true"""
    if searchPat('a*t*r','Some anteaters are nice') == True:
        print('Pass')
    """Searches for a,t, and r separated by any amount of characters in The albatross was hanging by its neck and checks to see if its true"""
    if searchPat('a*t*r','The albatross was hanging from its neck') == True:
        print('Pass')
    """Searches for a,t, and r separated by any amount of characters in The artist painted and checks to see if its true"""
    if searchPat('a*t*r','The artist painted') == False:
        print('Pass')
    """Searches for a,t, and r separated by any amount of characters in The artist worked and checks to see if its true"""
    if searchPat('a*t*r','The artist worked') == True:
        print('Pass')
test()

