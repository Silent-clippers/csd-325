# Keanu Foltz mod 8.2 CSD 325 12/8/24
# this program appends and shows json file

import json
from os import path

filename = r'C:\csd\csd-325\module-8\student.json'

with open(filename) as file:
    students = json.load(file)

def print_student_info(filename):
        for student in students:
            print(f"{student['F_Name']}, {student['L_Name']}: ID = {student['Student_ID']}, Email = {student['Email']}")
                  
print_student_info(filename)
print("This is the original student list.")

def update_student_info(filename):
    students.append({"F_Name": "Keanu",
        "L_Name": "Foltz",
        "Student_ID": 19955,
        "Email": "kfoltz@gmail.com"})

update_student_info(filename)

with open(filename, 'w') as json_file:
    json.dump(students, json_file,
                        indent=4,
                        separators=(',',': '))

print_student_info(filename)
print('This is the updated student list.')