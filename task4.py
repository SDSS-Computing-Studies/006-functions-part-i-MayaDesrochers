#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

import math
def isInteger(a):
    a=float(a)
    
    if math.floor(a)==a:
        x=True
        return x
    else:
        x=False
        return x

    
    
