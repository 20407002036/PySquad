#!/usr/bin/python3

"""
Array of nums has n distinct nums of range [0, n]

Return: The number in the range that is not in the array
"""

def getmissing(array):
    array.sort()

    n = array[0]
    newArray = []

    for element in array:
        if n != element:
            newArray.append(n)


        n+=1
        
    print(newArray)

nums = [1,4,6,3,2]
getmissing(nums)
