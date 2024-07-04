# Python Class

class Student: 
    def __init__(self, name, age, grade): 
        self.name = name 
        self.age = age 
        self.grade = grade

student1 = Student('Neeraj', 12, 'A') 

print(student1.name)   
print(student1.age)    
print(student1.grade)  
print(Student.__doc__)    
print(Student.__name__)   
print(Student.__module__) 
print(Student.__bases__)   
print(Student.__dict__)    
student2 = Student("A", 1, "A") 
student3 = Student("B", 2, "B")

del student2
del student3
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def displayStudent(self):
        return "Student name is " + self.name + " and age is " + str(self.age)
student1 = Student("BOB", 21, "A")
print(student1.displayStudent())
