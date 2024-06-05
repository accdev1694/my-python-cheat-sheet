# lets create a sorted list of dictionaries
# lets start by appending the file content into my empty list
students = []

with open('names.csv') as file:
    for line in file:
        line = line.rstrip().split(",")
        name, location = line[0], line[1]
        student = {'name': name, 'location':location}
        students.append(student)
        
for student in students:
    print(student['name'], 'is in', student['location'])