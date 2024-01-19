def countdig(num):
    count=0
    while(num>0):
        num=num//10
        count+=1
        
    print(count)

n=int(input("enter the value"))
countdig(n)
        