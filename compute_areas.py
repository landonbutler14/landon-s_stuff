#This Program computes the area of different three different shapes: circle, rectangle, and triangle.

def compute_area_circle(radius):
    import math
    return math.pi * radius ** 2
def compute_area_rectangle(length, width):
    return length * width   
def compute_area_triangle(base, height):
    return 0.5 * base * height  

print("Welcome to the Area Calculator!")
shape = input("Enter the shape (circle, rectangle, triangle): ").lower()
if shape == "circle":
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = compute_area_circle(radius)
        print(f"The area of the circle is: {area:.2f}")
    except ValueError:
        print("Invalid input, please enter a numeric value for radius.")
elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = compute_area_rectangle(length, width)
    print(f"The area of the rectangle is: {area:.2f}")
elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = compute_area_triangle(base, height)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("Invalid shape entered. Please choose circle, rectangle, or triangle.")
    restart = (input("Restart?")).lower()
    if restart == "yes" or restart == "y" or restart == "sure" or restart == "ok" or restart == "why not":
        exec(open("compute_areas.py").read())

input("Press Enter to exit")
