"""
take a list from input and check this list sorted or not.

"""

input_list= list(map(int, input("enter the list elements: ").split()))

result=input_list.copy()
result.sort()

if input_list==result:
    print("list is sorted")

else:
    print("list is not sorted")
