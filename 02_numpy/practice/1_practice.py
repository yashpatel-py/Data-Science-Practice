import numpy as np

# Q1 - Create Array
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(a)

# Q2 - Create 2 dimension array
# b = np.array([[1, 2], [1, 23], [12, 34]])
# print(b)

# Q3 - How know the dimensions of the array ?
# print(a.ndim) # one dimension
# print(b.ndim) # two dimension

# Q4 - How to change the data type of the array ?
# c = np.array([[1, 2], [1, 23], [12, 34]], dtype=int)
# print(c)

# Q5 - How to know size of the array ?
# print(c.size)

# Q6 - How to know shape of the array ?
# print(c.shape)

# Q7 - What does itemsize return?
# print(c.itemsize)

# Q8 - How to create matrix with zeros and once ?
# print(np.zeros([3,3], dtype=complex))
# print(np.ones([3,3], dtype=complex))

# Q9 - What is arange function ?
# d = np.arange(5, 20, 2)
# print(d)
# print(type(d))

# Q10 - What is linspace fucntion ?
# e = np.linspace(1,5,10)
# print(e)

# Q11 - Rehsape the exesting array.
# print(c.shape)
# print(c)
# print("------------")
# f = c.reshape(2, 3)
# print(f.shape)
# print(f)

# Q12 - Flat the array.
# print(c.ravel())

# Q13 - 13. Sum of the array.
# print(c.sum())

# Q14 - Find the minimum value and maximum value of the array.
# print(c.min())
# print(c.max())

# Q15 - Find the minimum value and maximum value of the array.
# print(c.sum(axis=1))

# Q16 - Sum only column of the array.
# print(c.sum(axis=0))

# Q17 - Find the sqrt of the array.
# print(np.sqrt(c))

# Q18 - Do some basic math operation on array.
g = np.array([[1, 2], [5, 6]])
h = np.array([[11, 22], [33, 44]])

print(g+h)
print(g-h)
print(g*h)
print(g/h)
print(g//h)
print(g**h)