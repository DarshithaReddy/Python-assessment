class AccessModifiers:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Public Constructor Called")
        elif b is None:
            self._value = a  # Protected Variable
            print("Protected Constructor Called")
        else:
            self.__value = a  # Private Variable
            print("Private Constructor Called")

# Creating Object
obj1 = AccessModifiers()      # Public Constructor
obj2 = AccessModifiers(10)    # Protected Constructor
obj3 = AccessModifiers(10, 20)  # Private Constructor

# Trying to access variables
print(obj2._value)  # Accessible but should be avoided (Protected)
# print(obj3.__value)  # This will give AttributeError (Private)
print(obj3._AccessModifiers__value)  # Correct way to access private attribute

