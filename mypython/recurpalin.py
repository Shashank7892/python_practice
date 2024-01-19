def ispalinrec(n,s,e):
    if s==e:
        return True
    if n[s]!=n[e]:
        return False
    if s<=e:
        return ispalinrec(n,s+1,e-1)
    return True

def ispalin(n):
    l=len(n)
    if l==0:
        return True
    return ispalinrec(n,0,l-1)

n=input("enter the value")
if(ispalin(n)):
    print("yes its a palindrome")
else:
    print("Nope its not a palindrome")