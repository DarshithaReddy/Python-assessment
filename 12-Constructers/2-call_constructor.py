class Parent:
    def __init__(self):
        print("Parent Default Constructor")

    def __init__(self, x):
        print(f"Parent Parameterized Constructor with value: ",x)

class Child(Parent):
    def __init__(self):
        super().__init__(100)  # Calling Parent's constructor
        print("Child Constructor")

# Create an object of Child class
c = Child()
