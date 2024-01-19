def factrec(n):
    if n==1:
        return n
    else:
        return n * factrec(n-1)
    
n=int(input("enter the number"))
print(factrec(n))