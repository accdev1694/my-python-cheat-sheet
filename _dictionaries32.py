# dictionaries keep record of keys and values

days = {
    "Day 1": "Sunday",
    "Day 2": "Monday",
    "Day 3": "Tuesday",
    "Day 4": "Wednesday",
    "Day 5": "Thursday",
    "Day 6": "Friday",
    "Day 7": "Saturday"    
}

# access the values by printing the key

print(days["Day 1"]) 

# we can as well use a for loop to print all the values

for day in days:
    print(days[day])
# when you use a for loop to iterate over a dictionary in python, it iterates over the keys
    
# interestingly, we can also print each key with its corresponsing value

for day in days:
    print(f"{day}: {days[day]}")