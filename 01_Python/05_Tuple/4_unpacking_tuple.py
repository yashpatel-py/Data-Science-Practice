# Packing tuple
# the_tuple = (1, 1.2, 23j, 'Yash', True, 'Patel')
# print(the_tuple)

# Unpacking tuple
# the_tuple = (1, 1.2, 23j, 'Yash', True, 'Patel')
# (int_num, float_num, complex_num, string_1, bool_num, string_2) = the_tuple
# print(int_num)
# print(float_num)
# print(complex_num)
# print(string_1)
# print(bool_num)
# print(string_2)

# ----------------------------------------------------------------
# using Astrisk*
the_tuple = (1, 1.2, 23j, 'Yash', True, 'Patel')
(int_num, float_num, *complex_num) = the_tuple
print(int_num)
print(float_num)
print(complex_num)
(int_num, *float_num, complex_num) = the_tuple
print(int_num)
print(float_num)
print(complex_num)