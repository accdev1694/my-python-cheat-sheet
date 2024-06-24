# lets sort a numbers list in ascending order

numbers = [1, 2, 4, 2, 12, 3]
print(sorted(numbers), "(sorted() function)")
print()
# the orted function returns a new list, the old list is preserved
print(numbers, "(original list preserved)")
print()

# the sort function modifies the original list
numbers.sort()

print(numbers, "(sort() function)")
