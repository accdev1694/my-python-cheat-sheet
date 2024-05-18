# you can split a string on a character and assign them to variables

name = input("Name: ")
first_name, last_name = name.split(' ')
# split on spaces

print(first_name, last_name)