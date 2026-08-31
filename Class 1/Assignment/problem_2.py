
price=float(input("enter the product's price: "))
quantity=int(input("enter the product's quantity: "))

result=float(price*quantity)

print("without tax the total amount is: ", round(result,2))

tax=float(result*0.05)
final_amount=result+tax

print("with tax the total amount is: ", round(final_amount,2))