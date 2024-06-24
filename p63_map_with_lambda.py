# lets map through a list  and get prices

items = [
    ("Rice", 21),
    ("Beans", 12),
    ("Yams", 23)
]
# first lets sort this list

items.sort(key=lambda item: item[1])
#print(items)

# next we map through and add prices to a variable
# we can also convert the prices into a list
prices = list(map(lambda item: item[1], items))

print(prices)