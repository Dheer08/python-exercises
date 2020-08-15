# 27. Write a Python program to concatenate all elements in a list into a string and return it.

list_data = [1,2,3,4,5]
output = ''
for i in list_data :
    output  += str(i)

print(output)
print(type(output))
