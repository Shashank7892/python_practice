def sums(n):
    if n==0:
        return 0
    return (1 + sums(n//10))

n=int(input("enter the n value"))
print(sums(n))
