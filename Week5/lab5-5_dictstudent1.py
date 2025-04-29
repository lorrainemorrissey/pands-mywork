# dictstudent1.py
# Lab 5.5 - programme to programme to us dictionaries to store inputed student information

# Author: Lorraine Morrissey

student = {
    "name":"Mary",
    "modules":[
        {"coursename":"Programming",
            "grade": 45
        },
        {"coursename":"History",
            "grade": 99}
    ]
}
print("student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t{} \t:{}".format(module["coursename"],module["grade"]))