def armstrong(n):
    s=len(n)
    v=0
    n=int(n)
    t=int(n)
    while n>0:
        dig=n%10
        v=v+(dig**s)
        n=n//10
        
    if t==v:
        print("yes its armstrong number")
    else:
        print("no its not a armstrong number")

n=input()
armstrong(n)  