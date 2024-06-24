# here we use a filter function to filter out prices that are less than or eual to a certain amount, into a new list

items = [
    ("Rice", 21),
    ("Beans", 12),
    ("Yams", 23)
]

prices = list(filter(lambda item: item[1] <= 21, items))
print(prices)

