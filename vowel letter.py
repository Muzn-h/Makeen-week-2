#How to the vowel letters in the given word 
s=input("enter a string")
count=0
s=s.lower()
print(s)
for i in s:
    if (i =="a" or i=="i" or i=="o" or i=="u" or i=="e"):
        count +=1
print(count)
