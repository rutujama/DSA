def printN(n):
    if n>=0:
        printN(n-1)
        print(n)
printN(10)

def reverseN(n):
    if n>0:
        print(n)
        reverseN(n-1)
reverseN(10)   
def oddN(n):
    if n>0:
        oddN(n-1)
        print(2*n-1)
oddN(9)    
def evenN(n):
    if n>0:
        evenN(n-1)
        print(2*n)
evenN(9) 
def RoddN(n):
    if n>0:
        print(2*n-1)
        RoddN(n-1)
RoddN(9)  
def RevenN(n):
    if n>0:
        print(2*n)
        RevenN(n-1)
RevenN(9)     