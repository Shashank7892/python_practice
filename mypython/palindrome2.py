def ispalindr(st,s,e):
    if e<=0:
        return True
    if s==e:
        return True
    if st[s]!=st[e]:
        return False
    if s<=e:
        return ispalindr(st,s+1,e-1)
    return True

st=input("enter the value")
e=len(st)
if(ispalindr(st,0,e-1)):
    print("yes its a palindrome")
else:
    print("no its not a palindrome")
