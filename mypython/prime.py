def prime(n):
    k=0
    for i in range(2,n//2+1):
        if(n % i ==0):
            k+=1
    if(k>1):
        print("its not a prime number")
    else:
        print("its a prime number")

n=int(input("enter the n value"))
prime(n)