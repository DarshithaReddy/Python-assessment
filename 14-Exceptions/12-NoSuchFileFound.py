class Example:
    def __init__(self):
        self.name = "Python"

obj = Example()
try:
    print(obj.age)  # 'age' is not defined
except AttributeError:
    print("Error: Attribute not found in the object")
