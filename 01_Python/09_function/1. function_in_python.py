# Creating simple fucntion
# def my_func():
#     print('Hello My 1st Fucntion')

# Arguments
# def my_func(name, age):
#     print('My name is ' + name + ", and i am " + age + " year old")

# def my_func2(name, age):
#     print('My name is ' + name + ", and i am " + age + " year old")

# my_func2("Yash Patel", "23")
# my_func("Manav", "21")

# -------------------------------------------------

# def details(*name):
#     print('My name is ', name[2])
#     print(type(name))

# details('yash', 'parth', 'manav', 'dhruv')


# def details2(**name):
#     pass

# details2(f_name = "yash", l_name="Patel")

# passing a list as an argument.
# def mu_func_list(names):
#     for x in names:
#         print(x)

# list_names = ["Yash Patel", "Dhruv Sutail", "Khushi Jani", "Shreya Patel"]

# mu_func_list(list_names)

# return value
def my_return_func(x):
    return 10 * x

print(my_return_func(5000))