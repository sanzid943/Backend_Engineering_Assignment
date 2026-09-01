"""
Create a = 200 and b = 200 , then print a is b . Do the same with 2000 . In a comment, explain in one line why one prints True and the other False (revisit the small-integer cache in Section 11).

"""


a=200
b=200

print(a is b)      # true (cached, same object)

a=2000
b=2000

print(id(a) is id(b))     # false (two separate objects)