class Example:
    def show(self, a, b):
        print("Method called with:",a,b)

obj = Example()
obj.show(10, 20)  # Always calls the latest defined method
