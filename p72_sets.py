# a set is simply a data type that doesn allow for duplicates
# sets are unordered collections
num = [1,1,3,4,5,5]
set1 = set(num)
print(set1)
# you can add, append, remove and use the len() with sets

#sets support powerful math operations

# get the union of 2 sets
set2 = {1,4,5}
print(set1 | set2)

# get the intersection of the two sets
print(set1 & set2)

# get the difference between two sets
print(set1 - set2)

# get symmetric difference meaning characters in either set but not in both
print(set1 ^ set2)

# you can use conditionals in sets but not indexing