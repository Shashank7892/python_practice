def countrec(n):
    if n==0:
        return 0
    return (1 + countrec(n//10))

n=int(input("enter the value"))
print(countrec(n))