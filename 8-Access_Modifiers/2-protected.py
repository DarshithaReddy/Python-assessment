class ProtectedDemo:
    def __init__(self):
        self._protected_field = "This is a Protected Field"

    def _protected_method(self):
        print("This is a Protected Method")

class SamePackageClass:
    def access_protected(self):
        obj = ProtectedDemo()
        print(obj._protected_field)  # Accessible within the same package
        obj._protected_method()

# Subclass in a different file (simulating a different package)
class ChildClass(ProtectedDemo):
    def access_protected_from_child(self):
        print(self._protected_field)  # Accessible in subclass
        self._protected_method()

if __name__ == "__main__":
    print("\nAccessing Protected Members Within Same Package:")
    same_pkg = SamePackageClass()
    same_pkg.access_protected()

    print("\nAccessing Protected Members from Child Class:")
    child = ChildClass()
    child.access_protected_from_child()
