#by using funcation in python we get the polygon by input the number of  side and the length of them 
import math

 
def area(side, length):
        regualr_area = (side * (length ** 2)) / (4 * math.tan((math.pi) / side))
        
        return regualr_area,side,length
num_sides = int(input("Enter the number of sides: "))
length_side = float(input("Enter the side: "))

p_area = area(num_sides,length_side)
    
print(p_area)