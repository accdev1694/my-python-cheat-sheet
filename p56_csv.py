# csv is comma seperated values

# it is used to seperate various values with commas
'''
with open('names.txt') as file:
    for line in file:
        name, gender = line.strip().split(",")
        print(f"{name} is {gender}")'''
        

names_location = []
for _ in range(3):
    names_location.append(f"{input("Name: ")}\n")

with open('names.csv', 'w') as file:
    for name in names_location:
        name = name.replace(" ", ",")
        file.write(name)
    
