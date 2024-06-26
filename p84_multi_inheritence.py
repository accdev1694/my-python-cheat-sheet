# a child can inherit attributes from more than one parent
# similarly, multi-parent inheritence is also possible

class People():
    def __init__(self, name):
        self.name = name
    def sleeping(self):
        return f"{self.name} is sleeping"
    def eating(self):
        return f"{self.name} is sleeping"
    
class Parent(People):
    def lives(self):
        return f"{self.name} lives in Coventry"
    
class Teacher(People):
    def attends(self):
        return f"{self.name} goes to Coundon Primary"
        
class Student(Parent, Teacher):
    
    def in_school(self):
        return f"{self.name} is in school"
        
student = Student("Dan")
teacher = Teacher("Miss Johnson")

# lets use the students own attributes
print()
print(student.in_school())
print()

# lets get the student's parent attributes
print(student.lives())
print(student.attends())
print()

# lets get the grandparents attributes
print(student.sleeping())
print(student.eating())
print()

# we can see the teacher class as well

print()

# lets get the student's parent attributes
print(teacher.attends())
print()

# lets get the grandparents attributes
print(teacher.sleeping())
print(teacher.eating())
print()
