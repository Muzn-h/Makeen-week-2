#program check valid number 
str=input("Enter the number in the format ((xxx)xxx-xxxx)")
valid = len(str)== 13
posi = 0
while valid and posi < len(str):
    
    if posi == 0 :
        valid = str[posi] == "("
    elif posi == 4 :
        valid = str [posi] == ")"
    elif posi == 8:
        valid = str [posi] = "-"
    else:
        valid = str[posi].isdigit()
    posi +=1
if valid :
    print("The string contain a valid number")
else:
    print("The string does not contain a valid number")
        