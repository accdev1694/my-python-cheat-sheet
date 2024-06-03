# lets use the open function to write our previous names into a new file



names = []
for _ in range(5):
    names.append(input("What is your name? "))

file = open("names.txt", "w")
for name in sorted(names):
    file.write(name, end)
file.close()