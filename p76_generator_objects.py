from sys import getsizeof

# generator objects are used to minumize the use of memory in story large data sets

# unlike lists, they donr store values in memory, they simply generate new values in each iteration

values = [x * 2 for x in range(10)]
for value in values:
    print(value)
print("_____")
    
# now if we used a generator object by using paren' instead of squar brackets
values = (x * 2 for x in range(10))
print(values)
for value in values:
    print(value)
# we get the same results, but take a look at the object (<generator object <genexpr> at 0x0000028F05893780>)

# the difference is that their size is really small. import the getsizeof function from the sys module

# check the size of value for both the list and generator and compare

values = (x * 2 for x in range(10000))
print(getsizeof(values), "size for gen")

values = [x * 2 for x in range(10000)]
print(getsizeof(values), "size for list")

# imagine the difference. if you are dealing with a large data set, use generators
# however, they do not support len() function