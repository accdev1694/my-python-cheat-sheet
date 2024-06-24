# list comprehensions are very pythonic. heres another example:

values = []
for x in range(5):
    values.append(x * 2)
print(values)

print()

# for the above code, heres the equivalent list comprehension
values = [char*2 for char in range(5)]
print(values)