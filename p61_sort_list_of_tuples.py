# imagine a list of tuples from a sales, product and price

items = [
    ("rice", 20),
    ("beans", 23),
    ("oil", 21)
]
# sort this list by price

items.sort(key=lambda item: item[1])
print(items)
