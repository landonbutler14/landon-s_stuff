import math

# Function to compute the area of a regular pentagon

def areaRegularPentagon(lengthSide):
    lengthSide= int (lengthSide)
    pentagonArea = (5 * (lengthSide ** 2)) / (4 * math.tan(math.pi / 5))
    return pentagonArea

# This just plugs in "lengthSide" into the given formula for the area of a pentagon

def areaMultiplePentagons(numPentagons, lengthSide):
    numPentagons = int (numPentagons)
    totalArea = float(areaRegularPentagon(lengthSide) * numPentagons)
    return totalArea

lengthSide = input ("Please enter the side length of the pentagon: ")

while not lengthSide.isdigit():
    lengthSide = input ("Invalid Int: Please input valid integer:")



numPentagons = input("Please enter how many pentagons: ")

while not numPentagons.isdigit():
    numPentagons = input ("Invalid integer please enter again: ")
result = areaMultiplePentagons(numPentagons,lengthSide)

print(f"The final area of all pentagons is {result:.4f}")
input ("Press Enter to quit ")
