#  a tuple is a read-only list
# it uses parenthesis, or not. however if the item is only one, you should add a trailing comma so its not treated as a string or integer

# tuples with parenthesis
my_tuple = (1, 2, 3)
print(my_tuple)

# tuples without parenthesis
my_tuple = 3, 4, 5
print(my_tuple)

# tuples with one item and without paren'
my_tuple = 1,
print(my_tuple)

# tuples concatinated
my_tuple = (1, 2, 3) + (4, 5, 6)
print(my_tuple)

# tuples with multiplication operator
my_tuple = (1, 2, 3) * 4
print(my_tuple)

# convert a list to a tuple
my_tuple = tuple([1, 2, 3])
print(my_tuple)

# convert a string to a tuple
my_string = tuple('Hello World')
print(my_string)

# tuples are ordered, hence, indexed. meaning we can slice them
# you can iterate through them and use conditionals to them
# in the real world, when working with a sequence of objects, if you dont want to accidentally modify them, use tuples