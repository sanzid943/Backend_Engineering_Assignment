"""
Ask the user for a temperature in Celsius, then print it in Fahrenheit using the formula F = C * 9/5 + 32 . Remember to convert the input with float()

"""

temperature=float(input("enter the temperature in Celsius: "))

result=float((temperature*(9/5))+32)

print("the temperature in fahrenheit is: ", round(result,1))