import numpy as np

# a = np.array([1,2,3])
# print(a[0:2])
# print(a[-1])

# b = np.array([[1,2,3], [4,5,6], [6,7,8]])
# print(b[1,2])

# print(b)
# print(b[0:3,1])

# print(b[-1])
# print(b[-1, 0:2])

c = np.arange(12).reshape(3,4)
print(c)

d = c > 4
print(d)

print(c[d]) # This will returun the element wich where true in above array