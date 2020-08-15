'''
23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2
'''
given_string = input("Enter a string : ")
len_string = len(given_string)
if len_string > 2:
    our_string = given_string[0:2]
else :
    our_string = given_string[0:len_string]
n = int(input("Enter n value : "))
for i in range(n):
    print(our_string)
