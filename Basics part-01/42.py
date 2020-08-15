# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import struct
print(struct.calcsize("P") * 8)

import platform
print(platform.architecture())

import sys
print(sys.version)
