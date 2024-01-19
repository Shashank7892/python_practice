def pangram(s):
    List=[]
    
    for i in range(26):
        List.append(False)
    
    for ch in s.lower():
        if not ch==" ":
            List[ord(ch)-ord('a')]=True
            
    for c in List:
        if c==False:
            return False
    return True


s=input("enter the String")
if pangram(s):
    print("yes its a pangram")
else:
    print("no its not a pangram") 
