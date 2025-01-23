#Given the dictionary in the student_dict.py file, representing students and the
#list of each student’s grades, find the average of each student and then print students with an
#average lower than 40. The key is the id of each student.

#dictionary from the student_dict.py at:
#https://github.com/gprok-esc-courses/cs-fundamentals/blob/main/99-csv-files/student_dict.py
students = {
	10: {'name': 'Russell Lopez', 'grades': [45, 34, 67, 45, 0, 34]},
    11: {'name': 'Theresa Campbell', 'grades': [40, 34, 20, 44, 56, 18, 34, 35]},
    12: {'name': 'Martin Roy', 'grades': [46, 55, 71, 67, 55, 64]},
    13: {'name': 'Nicole Young', 'grades': [40, 38, 42, 42, 51]},
    14: {'name': 'Elizabeth Diaz', 'grades': [44]},
    15: {'name': 'Susan Coleman', 'grades': [56, 19, 55, 34, 30, 18]},

}

#check all students grades 
for student_id, data in students.items():
    grades = data['grades']
    
    #count for every avarage
    total = 0
    count = 0
    for grade in grades:
        total += grade
        count += 1
    average = total // count

    #if the avege is lower than 40 print the name and avarage
    if average < 40:
        print("Student:", data['name'], "Average:" ,average)