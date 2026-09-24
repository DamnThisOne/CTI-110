'''
J Greene
24.09.26
Using python math library to calculate circle features .
'''
import math
print(math.pi)

# Get Radius from user (float)
Radius = float(input("Enter the radius as a float: "))

print()

# Calculate diameter . smiles brightly .
Diamet = 2 * Radius

#display diameter using f string . smiles kindly
print(f"The diameter of the circle is {Diamet:.1f}")

print()

#calculae circumfrence

circum = 2 * math.pi * Radius

print(f"the circumfrence of the circle is {circum:.2f}")

print()

area = math.pi * math.pow(Radius, 2)

print(f"the area of the circle is {area:.3f}")