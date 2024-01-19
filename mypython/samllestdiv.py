def smalldiv(n,i):
    if(n==0):
        print("0")
    else:
        if i<=n:
            if n%i==0:
                print(i)
                exit()
            return smalldiv(n,i+1)

n=int(input("enter the n value"))
smalldiv(n,2)