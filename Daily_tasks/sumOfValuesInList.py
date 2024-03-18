#!/usr/bin/python3

def sumOfValues(list):
    """
    list of int

    [2,1,4,5,3,6,8,7]

    second largest = 7
    second smallest = 2

    sum(7, 2)
    
    Return: sum of 2ndlargest and second smallest int in the list
    """
    size = len(list)

    if size == 0:
        return(0)
    elif size == 1:
        return(list[0])
    else:
        list.sort()
        print(list)
        # num = []

        # print(len(num))

        a = len(list) -2

        return(list[1] + list[a])


def sumFromASet(list):
    size = len(list)

    if size == 0:
        return(0)
    elif size == 1:
        
        return(list[0])
    else:
        # create a set
        # iterate through the list appending the set when
        # new item is encounterd

        numberSet = set()
        for item in list:
            if item not in numberSet:
                numberSet.add(item)



def sumOfArray(list):
    """
    for Python has no built in array. list is commanly used for the same

    to find sum of elements in the Array.
    Assume that array has only ints

    use the sum function
    """

    return sum(list)
    
numbers = [2,1,4,5,3,6,8,7,8,8]
# print(sumOfValues(numbers))

# sumFromASet(numbers)

print(sumOfArray(numbers))

age = [21]
# print(sumOfValues(age))

cash = []
# print(sumOfValues(cash))
