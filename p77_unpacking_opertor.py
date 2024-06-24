# you can unpack any iterable directly to print

numbers = [1,2,3,4,5]
print(*numbers)

string = "Oloche"
print(*string)

my_dict = {"Oloche": 23, "Dan": 12}
print(*my_dict) # this gets the keys

my_tuple = ("23", 25, "Oloche")
print(*my_tuple)