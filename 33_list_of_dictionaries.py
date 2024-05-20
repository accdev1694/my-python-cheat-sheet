# when we have more than one value fora each key in a dictionary, it is imperative to create a list of dictionaries

days = [
    {"name": "Sunday", "num": "Day 1", "Weather": "Rainy"},
    {"name": "Monday", "num": "Day 2", "Weather": "Sunny"},
    {"name": "Tuesday", "num": "Day 3", "Weather": "Cloudy"},
    {"name": "Wednesday", "num": "Day 4", "Weather": "Sunny"},
    {"name": "Thursday", "num": "Day 5", "Weather": "Rainy"},
    {"name": "Friday", "num": "Day 6", "Weather": "Sunny"},
    {"name": "Saturday", "num": "Day 7", "Weather": "Cloudy"},
]

# here we have succeeded in using the dame fields for each key in each dictionary

# lets access the name of each dictionary
for day in days:
    print(day["name"], day["num"], day["Weather"], sep=", ")