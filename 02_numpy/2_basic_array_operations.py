import numpy as np

# one dimensional
# a = np.array([5,6,9])
# print(a[1])

# two dimensional
# a = np.array([[1,2], [3,2], [88,93]])
# print(a.ndim)

# a = np.array([[1,2], [3,2]], dtype=np.float64)
# print(a)
# print(a.ndim)
# print(a.itemsize)
# print(a.size)
# print(a.shape)

# a = np.array([[1,2], [3,2]], dtype=complex)
# print(a)

# a = np.zeros((3, 3))
# print(a)

# a = np.ones((3, 3))
# print(a)

# b = np.arange(1,6,2)
# print(b)

# b = np.arange(1,6,2)
# print(b)

# c = np.linspace(1,5,10)
# print(c)

# print(a.shape)
# d = a.reshape(2,3)
# print(d.shape)

# print(a.ravel())

# print(a.min())

# print(a.max())

# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))

# print(np.sqrt(a))

# print(np.std(a))

# -------------------------------------

a = np.array([[1, 2], [3, 2]])
b = np.array([[4, 3], [6, 7]])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

print(a.dot(b))