def get_honor_students(student_list):
    honor_students = []
    try:
        for student in student_list:
            if student["gpa"] > 3.5:
                honor_students.append({"Name": student["name"], "GPA": student["gpa"]})
    except KeyError:
        print("Error: Student data is missing a key")
    except TypeError:
        print("Error: Invalid data format")
    except ValueError as e:
        print(e)

    return honor_students

students = [
    {"name": "Umer", "gpa": 3.4},
    {"name": "Sidra", "gpa": 2.9},
    {"name": "Nida", "gpa": 3.8},
]
honor_students = get_honor_students(students)
print(honor_students)


# for student in honor_students:
# f-string to format the output string
#     print(f"Name: {student['Name']}, GPA: {student['GPA']}")