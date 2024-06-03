# each time you run the previous program, it overrites the 
# existing content of the file, if there was anything there
# to fic this, we use the a argument instead of w
# this time lets use an f string to get new lines for each name
# it turns out that if we use the with keyword before open, we do not need to explicitely close the file evrytime
names = []
for _ in range(5):
    names.append(input("What is your name? "))

with open("names.txt", "a") as file:    
    for name in sorted(names):
        file.write(f"{name}\n")
    file.close()
# if there is more code undeerneath not indented, 
# the file gets closed automatically