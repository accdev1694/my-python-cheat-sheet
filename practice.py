items = [
    ("yams", 21),
    ("beans", 23),
    ("eggs", 12)
]



prices = map(lambda item: item[1], items)
for price in prices:
    print(price)