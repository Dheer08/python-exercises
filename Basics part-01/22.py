# 22. Write a Python program to count the number 4 in a given list.

num = input("Enter a list of numbers :  ").split(" ")
count = 0
for i in num :
    if int(i) == 4:
        count = count + 1
print(count)
