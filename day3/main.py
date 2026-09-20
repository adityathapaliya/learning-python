#Students mark checking system
student_1 = {"name":"aditya","marks" :[40,88,96,99,83]}
student_2 = {"name":"girish","marks" :[68,79,45,78,85]}
student_3 = {"name":"sudip","marks" :[70,76,54,98,88]}
student_4 = {"name":"rushan","marks" :[57,78,56,99,93]}
student_5 = {"name":"alson","marks" :[50,88,86,79,63]}
marks = student_1["marks"]
marks.sort()
avg_marks= sum(marks)/5

if marks[0] < 40:
    print('fail')

else:
    print("student_name =",student_1["name"])
    print("average_marks = ", avg_marks)

    if avg_marks > 100:
        print("number is wrong")
    elif avg_marks  >= 80:
        print("Excellent")
    elif avg_marks  >= 60:
       print("good")
    elif avg_marks  >= 40:
       print("passed")
    else:
        print("invalid input")
#############################################################



