'''
8. Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.
'''

import numpy as np

a = np.array([1+1j,1+0j,4.5,3,2,2j])

print(np.isreal(a))
print(np.iscomplex(a))

print(np.isscalar(3.1))
print(np.isscalar([3.1]))