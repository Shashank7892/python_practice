def survive(soilders,pattern):
    prev=""
    while prev!=soilders:
        prev=soilders
        soilders=soilders.replace(pattern,"")
    return soilders if soilders else "Defeat"

s=input()
p=input()
print(survive(s,p))