import string

def wordCount(filename):
    openme=open(filename, 'r')
    st = openme.read()
    wc=0
    i=0
    n=0
    while i<len(st)-1:
        while st[n] not in string.whitespace and n<len(st)-1:
            n+=1
        wc+=1
        while st[n] in string.whitespace and n<len(st)-1:
            n+=1
        i=n
    print (wc)


def main():
    wordCount(input("Enter file"))
main()
