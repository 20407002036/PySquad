#!/usr/bin/python3

"""

"""


def sumOfValues(list):
    """
    list of int

    [2,1,4,5,3,6,8,7]

    second largest = 7
    second smallest = 2

    sum(7, 2)
    
    Return: sum of 2ndlargest and second smallest int in the list
    """

    list.sort()
    # num = [1,2,3,4,5,6,7,8]

    # print(len(num))

    a = len(list) -2

    return(list[1] + list[a])


numbers = [2,1,4,5,3,6,8,7]
print(sumOfValues(numbers))
