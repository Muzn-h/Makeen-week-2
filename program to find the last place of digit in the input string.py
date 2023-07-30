#program find the last place of digit in the input string 
string= input("Enter string")

found = False
posi = len(string)-1
while not found and posi >= 0:
    if string[posi].isdigit():
        found = True
    else:
        posi = posi - 1
if found :
    print("First digit occurs at position", posi)
else:
    print("The string does not contain a digit")
    