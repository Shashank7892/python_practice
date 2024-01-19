def fibo(n):
    fib1=0
    fib2=1
    if n==0:
        print(fib1)
    elif n==1:
        print(fib1,fib2)
    elif n>1:
        print(fib1)
        print(fib2)
        for i in range(n-1):
            fib=fib1+fib2
            fib1=fib2
            fib2=fib
            print(fib)
        
n=int(input("enter the number"))
fibo(n)