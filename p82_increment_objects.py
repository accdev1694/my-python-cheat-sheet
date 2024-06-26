class Student():
    year = 2024
    total_students = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Student.total_students += 1
        
student1 = Student("Oloche", 40, "Male")
student2 = Student("Comfort", 35, "Female")
student3 = Student("Dan", 30, "Male")
student4 = Student("Karolis", 23, "Male")

print()
print("---------------------------")
print(f"1. {student1.name}, {student1.age}, {student1.gender}")
print(f"2. {student2.name}, {student2.age}, {student2.gender}")
print(f"3. {student3.name}, {student3.age}, {student3.gender}")
print(f"4. {student4.name}, {student4.age}, {student4.gender}")
print("---------------------------")
print(f"Total in class = {Student.total_students}")
print("---------------------------")
print()
