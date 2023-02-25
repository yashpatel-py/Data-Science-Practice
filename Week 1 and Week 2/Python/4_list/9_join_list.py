the_list_1 = ["orange", "Mango", "kiwi", "pineapple", "banana"]
the_list_2 = [100, 2, 50, 75, 35, 50, 75, 88]

# Using + operator
# the_list_3 = the_list_1+the_list_2
# print(the_list_3)

# Append list 2 into list 1
# for x in the_list_2:
#     the_list_1.append(x)

# print(the_list_1)

# extend()
the_list_1.extend(the_list_2)
print(the_list_1)