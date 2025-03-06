class Sample:
    def display(self):
        print("Sample class method")

try:
    class_name = "NonExistentClass"  # This class does not exist
    cls = globals()[class_name]  # Trying to access an undefined class
    obj = cls()  # This will raise an error
except KeyError:
    print("Error: Class not found!")


