
while True:
    import random 
    lower=int(input("enter the lower limit"))
    upper=int(input("enter the upper limit"))
    random_number=random.randint(lower,upper)
    print("please guess a number between the range from",lower,"to",upper)
    chance=0
    while(chance<8):
        guess=int(input("please enter the number"))
        if(guess==random_number):
            print("hurry!!!! you guessed the right number")
            break
        else:
            print("Sorry! try another you have still chances",8-(1+chance))
            chance+=1
        if chance==8:
            print("sorry chances are over")
            print("the random to guess was",random_number)
            break
    break
