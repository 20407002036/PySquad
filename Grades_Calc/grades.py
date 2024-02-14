#!/usr/bin/python3


def calculate_average_grades(students):
    # create a list to hold the average grades.
    average_grades = []
    # loop through the list of students
    for student in students:
        # Each student has a name and list of grades
        name, grades = student
        
        # check if list of grades has grades
        if len(grades) > 0:
            average_grade = sum(grades)/len(grades)
        else:
            average_grade = 0
        average_grades.append((name, average_grade))
     # return a list containing appended average grades   
    return average_grades
    

students = [("Smart", [76, 23, 45]), ("James", [9, 30, 68]), ("Okal",[89, 92, 67])]

result = calculate_average_grades(students)
print(result)
