import numpy as np
import sys
import time

# creating array
a = np.array([1,2,3])
b = np.array([4,5,6])
# print(a)
# print(type(a))

# accessing the array
# print(a[0])

# size of the array
# list_1 = range(1000)
# print(sys.getsizeof(5)*len(list_1))

# array = np.arange(1000)
# print(array.size*array.itemsize)

# Measuring processing time
# SIZE = 100000

# l1 = range(SIZE)
# l2 = range(SIZE)

# a1 = np.arange(SIZE)
# a2 = np.arange(SIZE)

# start = time.time()

# # List
# start = time.time()
# result = [(x+y) for x,y in zip(l1,l2)]
# print("List", (time.time()-start)*1000)

# # numpy
# start = time.time()
# result = a1 + a2
# print("Numpy", (time.time()-start)*1000)