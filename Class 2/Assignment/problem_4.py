"""
Given an age and a boolean is_citizen , print whether the person can vote — must be 18+ and a citizen (use and ).

"""

age=int(input("enter the age: "))

is_citizen=input("are you a citizen (true/false): ")

if age>=18 and is_citizen == "true":
    print("the person can vote")

else:
    print("the person can not vote")