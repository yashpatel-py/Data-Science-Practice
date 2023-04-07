import numpy as np

# Looping
# a = np.array([[1,2,3], [4,5,6], [6,7,8]])
# for row in a:
#     print(row)

# for cell in a.flat:
#     print(cell)

# Stacking
# b = np.arange(6).reshape(3,2)
# c = np.arange(6, 12).reshape(3,2)
# print(np.vstack((b,c))) # vstack = Virtual Stack
# print(np.hstack((b,c))) # hstack = Horizontal Stack

# Splitting
# d = np.arange(30).reshape(2, 15)
# e = np.hsplit(d,2)
# e = np.vsplit(d,2)
# print(e)
# print(e[0])
# print(e[1])