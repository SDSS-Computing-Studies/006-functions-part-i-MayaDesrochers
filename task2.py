#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(a):


    numList=a
    numList.sort()


    b=len(numList)
    answer=numList[b-1]
    return answer


#a.sort()
#a[-1]
#return a 