# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math
x1,y1 = 1,2
x2,y2 = 1,3

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(dist)
