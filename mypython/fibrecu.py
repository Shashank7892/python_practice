def fibrec(n):
    if n<=1:
        return n
    else:
        return fibrec(n-1)+fibrec(n-2)

n=int(input("enter the number"))
for i in range(n):
    print(fibrec(i))
