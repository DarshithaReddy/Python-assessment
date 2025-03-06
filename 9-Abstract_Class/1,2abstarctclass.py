from abc import ABC, abstractmethod

class AbstractDemo(ABC):  # Abstract class
    def __init__(self):
        self.value = "This is a non-abstract method in AbstractDemo"

    @abstractmethod
    def abstract_method(self):  # Abstract method
        pass

    def non_abstract_method(self):  # Non-abstract method
        print("This is a non-abstract method in AbstractDemo")
        
class ChildClass(AbstractDemo):  # Subclass
    def abstract_method(self):  # Implementing abstract method
        print("This is the abstract method implemented in ChildClass")

# Creating an instance of ChildClass
child = ChildClass()
child.non_abstract_method()  # Accessing non-abstract method from parent class
