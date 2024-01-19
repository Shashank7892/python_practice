def reversenum(num):
    if num<10:
        print(num)
        return
    else:
        print(num%10,end='')
        reversenum(num//10)



n=int(input("enter the number"))
reversenum(n)