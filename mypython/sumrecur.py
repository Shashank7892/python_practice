
def sumrecur(num):
    if num==0:
        return 0
    else:
        return (num%10 + sumrecur(num//10))

n=int(input("enter the number"))
result=sumrecur(n)
print(result)