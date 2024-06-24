# in python, when you need to use a list  for a large data set, use an array, if not, stick with lists
# arrays are typed. you specify this as the first argument
from array import array

numbers = array("i", [1, 2, 3, 4])
# you can use list methods to modify the array

