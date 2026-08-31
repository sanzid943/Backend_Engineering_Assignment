
a= 50

number=(input("enter any number: "))

result=a+number
print(result)          # TypeError: unsupported operand type(s) for +: 'int' and 'str'


number=int(input("enter any number: "))         #fixed code
result=a+number

print(result)