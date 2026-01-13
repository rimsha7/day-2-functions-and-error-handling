from function import get_honor_students
students = [
    {"name": "Umer", "gpa": 3.9},
    {"name": "Sidra", "gpa": 2.9},
    {"name": "Nida", "gpa": 3.55},
]
honor_students = get_honor_students(students)
for student in honor_students:
    #f-string to format the output string
    print(f"Name: {student['Name']}, GPA: {student['GPA']}")