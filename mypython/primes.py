def primes(n):
    k=0
    for i in range(2,n//2+1):
        if n%i==0:
            k+=1
    if k<=0:
        print("its a prime")
    else:
        print("not")
        
p=int(input())
primes(p)