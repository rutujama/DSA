def printN(n):
    if n>=0:
        printN(n-1)
        print(n)
printN(8)

def reverseN(n):
    if n>0:
        print(n)
        reverseN(n-1)
reverseN(10)   
