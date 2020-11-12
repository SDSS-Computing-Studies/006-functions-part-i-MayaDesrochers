#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math 
def hypotenuse(x,y,z):
    x=float(x)
    y=float(y)
    while z==False:
        if x>y:
            larger_number=x
            return larger_number
        elif x<y:
            larger_number=y
            return larger_number
    
    if z==True:
        answer=math.sqrt((x**2) +(y**2))
        return answer



