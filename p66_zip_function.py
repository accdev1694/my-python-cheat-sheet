# the zip function in python is really powerful
# you can use it to create a new list of tuples from a number of lists
list1 = "xyz"
list2 = [21, 22, 25]
list3 = [6, 34, 12]


my_zip = list(zip(list1, list2, list3))
for list in my_zip:
    print(list)