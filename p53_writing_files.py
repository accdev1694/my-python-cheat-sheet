# lets use the open function to write our previous names into a new file
# use the with keyword to open and close tha file automatically


names = []
for _ in range(3):
    names.append(input("What is your name? "))

with open("names.txt", "w") as file:
    
    for name in sorted(names):
        file.write(f"{name}\n")
