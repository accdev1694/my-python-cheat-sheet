# we can achieve the same results of the filter and map functions using list comprehensions

products = [
    ("Rice", 21),
    ("Beans", 12),
    ("Yams", 23)
]

# lets start by filtering all prices less than or equal to 21 into the prices list
prices = [product for product in products if product[1] <= 21]
print(prices)

# secondly lets map all prices to  a new list
only_prices = [product[1] for product in products]
print(only_prices)

