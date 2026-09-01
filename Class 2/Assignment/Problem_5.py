"""
Store a username and password, ask the user to enter them, and print success or failure using and.

"""

username="admin"
password="admin123"

input_username= str(input("enter username: "))
input_password= str(input("enter password: "))

if username==input_username and password==input_password:
    print("successful")

else:
    print("failed")