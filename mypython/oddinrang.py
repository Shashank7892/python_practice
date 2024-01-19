def oddinreg(l,u):
    for i in range(l,u+1):
        if(i % 2 !=0):
            print(i)
l=int(input("enter the Lower limit"))
u=int(input("enter the upper limit"))
oddinreg(l,u)