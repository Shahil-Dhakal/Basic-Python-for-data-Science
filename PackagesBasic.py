"""
Let's say you wanted to calculate the circumference and area of a circle. Here's what those formulas look like:
Rather than typing the number for pi, you can use the math package that contains the number
For reference, ** is the symbol for exponentiation. For example 3**4 is 3 to the power of 4 and will give 81.
"""
import math as mt
# Definition of radius
r = 0.43
# Calculate C
C = 2* mt.pi * r
# Calculate A
A = mt.pi * r**2
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

#----------------------------------------

# Import pi function of math package
from math import pi
# Calculate C
C = 2 * 0.43 * pi
# Calculate A
A = pi * 0.43 ** 2
print("Circumference: " + str(C))
print("Area: " + str(A))