'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
import math
radius_circle = float(input("Enter radius of a circle : "))
area = math.pi*radius_circle*radius_circle
# area2 = (22/7)*radius_circle*radius_circle
print(area)
