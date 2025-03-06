class Example:
    def show(self, a, b=None):
        if b is None:
            print(f"Single parameter: {a}")
        else:
            print(f"Two parameters: {a}, {b}")

obj = Example()
obj.show(10)         # Calls method with one parameter
obj.show(10, 20)     # Calls method with two parameters
