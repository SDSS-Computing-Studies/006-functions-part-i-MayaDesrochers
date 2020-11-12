#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(a):
    a=float(a)
    if a**2%(a**2)==1:
        x=True
        return x
    elif a**2%(a**2)>1:
        x=False
        return x

    
    
