# even or odd using recursion

def check(n):
    if(n<2):
        return(n % 2 == 0)
    return(check(n-2))

n=int(input("enter the number"))
print(check(n))
if(check(n)==True):
    print("even")
else:
    print("odd")