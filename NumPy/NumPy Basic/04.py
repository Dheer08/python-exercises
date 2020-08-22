# 4. Write a NumPy program to test whether any of the elements of a given array is non-zero.

import numpy as np

x = np.array([0,0,0,0,0])

if np.any(x) == True :
	print("Given array contains non-zero elements")
else :
	print("Given array contains no non-zero elements")