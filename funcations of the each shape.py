import math


#  function for square
def square_area(side):
    s_area = side ** 2
    return s_area

#  function for circle
def area_of_circle(radius):
    c_area = math.pi * radius**2
    return c_area

#  function for rectangle
def area_of_rectangle(length, width):
    r_area = length * width
    return r_area

#  function for cylinder
def area_of_cylinder(radius, height):
    total_area = (2 * math.pi * radius *  height) + (2 * math.pi * (radius ** 2))
    return total_area

#  function for triangle
def area_of_triangle(base, height):
    t_area = (base * height) / 2
    return t_area

#choose the shape number 
def main():
    while True:
        print("Choose the shape to calculate the area must choose from (1-6):")
        print("1-Square")
        print("2-Circle")
        print("3-Rectangle")
        print("4-Triangle")
        print("5-Cylinder")
        print("6-Quit")
        
        choice = int(input("Choice from  (1-6): "))
#depends on the entered shape that user input it will calculate the area of it as the required input of the area rule of the shape
        if choice == 1:
            side_length = float(input("Enter the side length of the square: "))
            sqr_area = square_area(side_length)
            print("The area of the square is:", sqr_area)

        elif choice == 2:
            radius = float(input("Enter the radius of the circle: "))
            circle_area = area_of_circle(radius)
            print("The area of the circle is: ", circle_area )

        elif choice == 3:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rectangle_area = area_of_rectangle(length, width)
            print("The area of the rectangle is:", rectangle_area)

        elif choice == 4:
            base = float(input("Enter the length of the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            triangle_area = area_of_triangle(base, height)
            print("The area of the triangle is", triangle_area)

        elif choice == 5:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            total_surface_area = area_of_cylinder(radius, height)
            print("The total surface area of the cylinder is:", total_surface_area)
#once the user entered 6 it will directly exit the program 
        elif choice == 6:
            print("Exit the program!")
            break
        else:
            print("Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()        