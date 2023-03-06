# try:
#   x = 1
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# finally:
#   print("Passed through try and except ")

x = 5
if x < 10:
  raise Exception("The number is below 10")