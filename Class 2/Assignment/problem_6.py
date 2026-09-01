"""
input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
input_list2 = [5,6,7,8,9,1,2,3,4,5,6]

do it for all methods:

.append
.insert
.extend
.remove
.pop()
.sort() / .reverse()
.count(x) / .index(x)

"""

input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
input_list2 = [5,6,7,8,9,1,2,3,4,5,6]


input_list1.append(10)
input_list1.insert(3,35)
input_list1.remove(4)
input_list1.pop(2)
input_list1.sort()
input_list1.reverse()
input_list1.extend(input_list2)

print(input_list1.index(10))
print(input_list1.count(3))


print(input_list1)



