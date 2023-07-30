#check valid entered cvv 
str=input("Enter the cvv in the format xxxx-xxx")
valid = len(str)== 8
posi = 0
while valid and posi < len(str):
    if posi == 4 :
        valid = str [posi] == "-"
    else:
        valid = str[posi].isdigit()
    posi += 1
    
if valid :
    print("The string contain a cvv")
else:
    print("The string does not contain a valid ccv ")