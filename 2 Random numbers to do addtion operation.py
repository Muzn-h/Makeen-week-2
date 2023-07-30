#generate 2 random numbers and ask question to answer

from random import randint


while 1: #while 1 is true 
    A = randint(1,10)
    B = randint(1,10)
    Addtional = A + B
    print("First number" ,A)
    print("Second number:", B)
    
    result =input("enter your result :")
    
    
    if (result!="done"):
        if (Addtional== int(result)):
            print("That's correct answer")
        else:
            print("That's wrong answer")
    else:
        break
    

                
    


 


        
    
    
    
   

  

