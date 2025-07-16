def printN(n):
    if n==1:
        return 1
    s=n+printN(n-1)
    return s
print("sum is:",printN(10))