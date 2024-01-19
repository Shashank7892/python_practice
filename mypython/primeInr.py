def primeinr(l,u):
    for i in range(l,u+1):
        k=0
        for j in range(2,i//2+1):
            if(i%j==0):
                k+=1
        if(k<=0):
            print(i)

l=int(input("enter the lower limit"))
u=int(input("enter the upper limit"))

primeinr(l,u)
