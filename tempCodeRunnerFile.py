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
print("odd sum is:",oddS(18)) 
def evenS(n):
    if n==1:
        return 1
    return 2*n+evenS(n-1)
print("even sum is:",evenS(16)) 
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print("factorial is:",fact(15))
def sqrN(n):
    if n==1:
        return 1
    return (n*(n+1)*(2*n+1))/6
print("sqr of n:",sqrN(8)) 