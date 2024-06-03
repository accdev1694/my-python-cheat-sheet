# you can read files using the r argument in the open function as follows
# you can sort the content as well


with open("names.txt", "r") as file:    
    for line in sorted(file):
        print("Hello", line.rstrip())