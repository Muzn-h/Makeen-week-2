#guessing game
import random 

num = random.randint(1, 10)

Guess = 0
while Guess != num:
    Guess = int(input("enter a number:"))
    
    if (Guess== num):
            print("That's correct answer")
            break
    elif (Guess > num):
        print("The number is less than the correct answer")
    else:
        print("The number is greater than the correct number")
        


    


