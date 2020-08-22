# Write a NumPy program to test element-wise for positive or negative infinity.

import numpy as np

a = np.array([1,0,np.nan,np.inf])

print(np.isinf(a))