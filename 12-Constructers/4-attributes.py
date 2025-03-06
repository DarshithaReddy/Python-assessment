class Student:
    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age

    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Creating object
s1 = Student("Alice", 22)
s1.display()

