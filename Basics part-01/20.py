#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

given_string = input("Enter a string : ")
n = int(input("Enter n value : "))

for i in range(n):
    print(given_string)
