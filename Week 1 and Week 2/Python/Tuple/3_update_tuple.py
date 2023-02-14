# Change tuple values
# the_tuple = (1, 1.2, 23j, "Yash", True)
# x = list(the_tuple)
# x[1] = 2
# the_tuple = tuple(x)
# print(the_tuple)

# ----------------------------------------------------------------
# Adding a new item
# the_tuple = (1, 1.2, 23j, "Yash", True)
# y = list(the_tuple)
# y.append("Patel")
# new_tuple = tuple(y)
# print(new_tuple)

# the_tuple = (1, 1.2, 23j, 'Yash', True, 'Patel')
# y = ("Truck",)
# the_tuple += y
# print(the_tuple)

# ----------------------------------------------------------------
# Removing items
the_tuple = (1, 1.2, 23j, 'Yash', True, 'Patel')
# y = list(the_tuple)
# y.remove(1.2)
# new_tuple = tuple(y)
# print(new_tuple)

# Deleting the tuple
del the_tuple
print(the_tuple)