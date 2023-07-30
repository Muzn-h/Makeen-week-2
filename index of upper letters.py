#Find the index of the upper letters 
s=input("Enter sentence")
for i in range(len(s)):
    if s[i].isupper():
        print(i)