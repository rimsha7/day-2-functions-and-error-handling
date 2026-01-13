# def my_function():
#     print("Hello")
# def func_arg(name):
#     print("Hello",name)
# my_function()
# func_arg("Rimsha")
# def add(a,b):
#     return a+b
# result = add(7,20)
# print(result)

def get_honor_students(student_list):
    honor_students = []
    for student in student_list:
        if student["gpa"] > 3.5:
            honor_students.append({"Name": student["name"], "GPA": student["gpa"]})
    return honor_students