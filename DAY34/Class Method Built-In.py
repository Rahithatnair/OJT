class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

Student1 = Student("A", 21, "A")

print(hasattr(Student1, "age")) 
print(hasattr(Student1, "marks"))  

setattr(Student1, "marks", "75")
print(hasattr(Student1, "marks"))  
print(getattr(Student1, "grade"))  
print(getattr(Student1, "name"))  
delattr(Student1, "marks")
print(hasattr(Student1, "marks"))  