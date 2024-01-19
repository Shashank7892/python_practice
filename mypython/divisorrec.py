def divrecur(n,i):
    if n==0:
        print("0")
    else:
        if i<=n:
            if n%i==0:
                print(i)
            return divrecur(n,i+1)
    

n=int(input("enter the n value"))
divrecur(n,1)
        