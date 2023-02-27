#! python3
import math 
h = input("Enter the height here:")
r = input("Enter the radius here:")
pi = 22 / 7
H = float(h)
R = float(r)
sa = (pi * R) * (R + (math.sqrt((H ** 2) + (R ** 2))))
print(sa)

# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
