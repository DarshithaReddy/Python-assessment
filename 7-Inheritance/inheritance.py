# Superclass A
class A:
    def __init__(self):
        self.value = "Class A Variable"

    def method_A1(self):
        print("Method A1: Specific to Class A")

    def method_A2(self):
        print("Method A2: Specific to Class A")

    def override_method(self):
        print("Override Method in Class A")

# Subclass B (Inherits from A)
class B(A):
    def __init__(self):
        super().__init__()
        self.value = "Class B Variable"

    def method_B1(self):
        print("Method B1: Specific to Class B")

    def method_B2(self):
        print("Method B2: Specific to Class B")

    def override_method(self):
        print("Override Method in Class B")

# Subclass C (Inherits from B)
class C(B):
    def __init__(self):
        super().__init__()
        self.value = "Class C Variable"

    def method_C1(self):
        print("Method C1: Specific to Class C")

    def method_C2(self):
        print("Method C2: Specific to Class C")

    def override_method(self):
        print("Override Method in Class C")

# Main class
if __name__ == "__main__":
    # Creating objects for each class
    objA = A()
    objB = B()
    objC = C()

    print("\nCalling methods using class instances:")
    objA.method_A1()
    objA.method_A2()
    objA.override_method()

    objB.method_B1()
    objB.method_B2()
    objB.override_method()

    objC.method_C1()
    objC.method_C2()
    objC.override_method()

    print("\nCalling overridden method using superclass reference:")
    refB: A = B()  # Superclass reference pointing to subclass B object
    refC: A = C()  # Superclass reference pointing to subclass C object
    refB.override_method()  # Calls B's method
    refC.override_method()  # Calls C's method

    print("\nRuntime Polymorphism with Data Members:")
    print("Value from objA:", objA.value)
    print("Value from objB:", objB.value)
    print("Value from objC:", objC.value)

    refB = B()
    refC = C()
    print("Value from refB (A reference to B):", refB.value)
    print("Value from refC (A reference to C):", refC.value)
