"""
Write a program that intentionally causes a string from TypeError (hint: add a number to a input() ). Run it, copy the error message into a comment, then fix the code so it works. This trains you to read errors — the most important debugging skill.

"""


a= 50

number=(input("enter any number: "))

result=a+number
print(result)          # TypeError: unsupported operand type(s) for +: 'int' and 'str'


number=int(input("enter any number: "))         #fixed code
result=a+number

print(result)