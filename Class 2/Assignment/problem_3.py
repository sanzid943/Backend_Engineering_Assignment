"""
Extend the in-class grading system: validate 0–100, then print the grade with if/elif/else

"""

number=float(input("enter the marks between 0 to 100: "))

if number>=80:
    print("grade: A+")

elif number>=70:
    print("grade: A")

elif number>=60:
    print("grade: A-")

elif number>=50:
    print("grade: B")

elif number>=40:
    print("grade: C")

elif number>=33:
    print("grade: D")

else:
    print("grade: F")


