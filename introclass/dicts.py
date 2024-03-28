#!/usr/bin/python3
"""
list = [1,2,3,4,5,6]

task 1 = time, state, description

shirt : clo....


task = {'name': 'Write your book', 'time': '8:00PM', 'Desc': 'the book ...'}

"""
"""
name
Gender
age
unit
"""

student = {'name': 'Mark', 'Gender': 'M', 'age': 23, 'units': ['CompScie', 'Geo']}


# student['Phone'] = '073773373'
# add phone and id No
# 
# student.get('name', 0)

# print(len(student))

for key, value in student.items():
    print(key, value)
