
a=200
b=200

print(a is b)      # true (cached, same object)

a=2000
b=2000

print(id(a) is id(b))     # false (two separate objects)