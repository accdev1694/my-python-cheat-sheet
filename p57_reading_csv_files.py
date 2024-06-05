# let us now read tha last created csv file and add a text to each nefore printing

with open("names.csv") as file:    
    for line in file:        
        name, location = line.rstrip().split(",")
        print(f"{name} is in {location}")