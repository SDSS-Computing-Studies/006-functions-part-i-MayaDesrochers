#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance( (a,b), (c,d)):
    a=float(a)
    b=float(b)
    c=float(c)
    d=float(d)
    answer1=(c-a)**2
    answer2=(d-b)**2
    answer3=math.sqrt(answer1+answer2)
    return answer3

