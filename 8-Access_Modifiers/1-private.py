class PrivateDemo:
    def __init__(self):
        self.__private_field = "This is a Private Field"

    def __private_method(self):
        print("This is a Private Method")

    def access_private(self):
        print(self.__private_field)  # Accessing private field inside class
        self.__private_method()      # Calling private method inside class

# Main method
if __name__ == "__main__":
    obj = PrivateDemo()
    obj.access_private()  # Allowed: Accessing private data inside the class

    # Attempting to access private members outside the class
    try:
        print(obj.__private_field)  # Error: Cannot access private field directly
    except AttributeError:
        print("Cannot access private field outside the class")

    try:
        obj.__private_method()  # Error: Cannot access private method directly
    except AttributeError:
        print("Cannot access private method outside the class")

# Subclass trying to access private members
class SubClass(PrivateDemo):
    def show_private(self):
        try:
            print(self.__private_field)  # Error: Private field not accessible
        except AttributeError:
            print("Subclass cannot access private field")

        try:
            self.__private_method()  # Error: Private method not accessible
        except AttributeError:
            print("Subclass cannot access private method")

sub_obj = SubClass()
sub_obj.show_private()
