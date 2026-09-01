"""
Ask the user for a number, then check with in whether it's in a given list. Print a friendly yes/no message with if/else

"""

input_list= [10, 14, 56, 34, 78, 24, 68]

number=int(input("enter a number: "))

if number in input_list:
    print("yes the number is in the list")

else:
    print("no the number is not in the list")


    