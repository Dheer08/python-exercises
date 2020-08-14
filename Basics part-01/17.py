# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000

num = int(input("Enter a number : "))

if num < 100 :
    print(str(num) + " is less than 100")
elif num > 100 and num < 1000 :
    print(str(num) + " is less than 1000 and greater than 100")
elif num > 1000 and num < 2000 :
    print(str(num) + " is less than 2000 and greater than 1000") 
