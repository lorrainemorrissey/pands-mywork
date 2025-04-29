# dictstudent.py
# Lab 5.4 - programme to us dictionaries to store student information

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