#program to get he maximum number by using funcation

A=int(input("enter the first number:"))
B=int(input("enter the second number:"))
C=int(input("enter the third number:"))
def maximum(A,B,C):
    
    if(A>=B and A>=C):
        return A
    elif (B>=A and B>=C):
        return B
    else:
        return C

    return maximum
maximum_number = maximum(A,B,C)
print("The maximum number is :",maximum_number)

