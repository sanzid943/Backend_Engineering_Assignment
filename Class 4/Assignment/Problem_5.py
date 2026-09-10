"""
Check whether a dictionary has an "email" key. Print it if present, otherwise "Email not found" — use .get() or in .

"""

input_student= {
    "name": "Rafsan",
    "age" : 25,
    "ID" : 101,
    "email" : "user@email.com",
}

value= input_student.get("email");

if value:
    print("Email: ", value)

else:
    print("Email not found")