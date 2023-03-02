the_set_1 = {True, 1, 2.1, 2e3j, "Yash Patel"}
the_set_2 = {"Truck", "bike", "car", "Yash Patel"}

# union
# the_set_3 = the_set_1.union(the_set_2)
# print(the_set_3)

# update
# the_set_1.update(the_set_2)
# print(the_set_1)

# Keep ONLY the Duplicates
# the_set_1.intersection_update(the_set_2)
# print(the_set_1)

# z = the_set_1.intersection(the_set_2)
# print(z)

# Keep All, But NOT the Duplicates
# the_set_1.symmetric_difference_update(the_set_2)
# print(the_set_1)

z = the_set_1.symmetric_difference(the_set_2)
print(z)