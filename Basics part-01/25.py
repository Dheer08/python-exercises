'''
25. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

data = [1,5,8,3]
num = int(input("Enter a number : "))
flag  = False
for i in data :
    if i == num :
        flag = True
print(flag)
