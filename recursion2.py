def printN(n):
    if n==1:
        return 1
    s=n+printN(n-1)
    return s
print("sum is:",printN(10))
def oddS(n):
    if n==1:
        return 1
    return 2*n-1+oddS(n-1)
print("odd sum is:",oddS(10)) 