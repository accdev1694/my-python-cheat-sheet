# they use key value pairs

# define a dictionary
my_dict = {"loch": 24, "Dan": 36, "comfort": 30}
print(my_dict)

# another way to define a dictionary
my_dict = dict(loch=24, Dan=36, comfort=30)
print(my_dict)


# check if a key exists
if "Dan" in my_dict:
    print('Yes')
    
# add new keys

my_dict["Loche"] = 31
print(my_dict)

# the get method is used to get the value of a key
print(my_dict.get("Nnanna"))    # returns none cos it doesnt exist

# you can add a n alterntive value if it doesnt exist
print(my_dict.get("Nnanna", 0))    # returns 0 by default cos it doesnt exist

# delete
del(my_dict["Loche"])
print(my_dict)

# looping over dictionaries
print()
for key, value in my_dict.items():
    print(key, value)