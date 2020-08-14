'''
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
'''

given_string = input("Enter string : ")
if given_string[0:2] != "Is":
    new_string = "Is " + given_string
else:
    new_string = given_string
print(new_string)
