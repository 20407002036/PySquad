#!/usr/bin/python3

"""
list - data of diferent types
Tuples -
Range
Dict - 
sets
"""

# list
students = ["John", "Jane", 34, 34, "John"]

print(type(students))
print(type(students[0]))
print(type(students[2]))

name = "MNU"
students.append(name)

print(students)


# Tuples
counties = ("Nai", "Kiambu", "Mom", "Nai")
print(len(counties))


# Dict
"""
Key: value
Calc: Explanation
"""

student = {
    "Name": "Lydia",
    "Age": 18,
    "Units": ["Python", "Java", "js"]
    }

print(student)
print(len(student))
