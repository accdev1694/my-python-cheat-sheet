# lets create a sorted list of dictionaries
# lets start by appending the file content into my empty list
students = []

with open('names.csv') as file:
    for line in file:
        line = line.rstrip().split(",")
        name, location = line[0], line[1]
        student = {'name': name, 'location':location}
        students.append(student)
        
def get_name(student):
    return student['name']
        
for student in sorted(students, key=get_name):
    print(student['name'], 'is in', student['location'])
    
#you may sort by name, location, in reverse or otherwise, as well