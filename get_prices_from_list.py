# we can create a new list of ptices from a list of tuples containing products and prices

items = [
    ("rice", 21),
    ("beans", 22),
    ("yams", 15)
]

# lets begin by sorting the list by prices

items.sort(key = lambda item: item[1])
for item in items:
    print(item)
print()

# create a new list of products
products = []
for item in items:
    products.append(item[0])
for product in products:
    print(product)
print()
# we can as well create a new list of prices
prices = []
for item in items:
    prices.append(item[1])
for price in prices:
    print(price)
