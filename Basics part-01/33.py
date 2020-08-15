# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = 10
b = 20
c = 30

if a == b or b == c or a == c:
    sum = 0
else :
    sum = a+b+c

print(sum)
