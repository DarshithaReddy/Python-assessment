class Example:
    def show(self, a):
        if isinstance(a, int):
            print(f"Integer method: {a}")
        elif isinstance(a, str):
            print(f"String method: {a}")

obj = Example()
obj.show(10)         # Calls the integer version
obj.show("Hello")    # Calls the string version
