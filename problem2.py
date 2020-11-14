#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
def distance(coord1,coord2):
    
    (x1,y1)=coord1
    (x2,y2)=coord2
    x1=float(x1)
    x2=float(x2)
    y1=float(y1)
    y2=float(y2)
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
