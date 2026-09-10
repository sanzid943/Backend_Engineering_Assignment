"""
Make a student dictionary, then print the name and age by their keys.

"""

input_student= {
    "name": "Rafsan",
    "age" : 25,
    "ID" : 101,
}

name= input_student.get("name")
age= input_student.get("age")

print("Name: ", name)
print("Age: ", age)


