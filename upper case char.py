#count upper letters in the given string 
s=input("Enter a string:")
uppercase =  0
for char in s:
    if char.isupper():
        uppercase += 1
print(uppercase)