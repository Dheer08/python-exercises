'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

'''

data  = input('Enter comma-separated data : ')
list_structure = list(data.split(','))
tuple_structure = tuple(data.split(','))

print(list_structure)
print(tuple_structure)

