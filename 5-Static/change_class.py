class Example:
    static_var = "Original Value"

    @classmethod
    def modify_static(cls):
        cls.static_var = "Changed at Class Level"

print("Before change:", Example.static_var)
Example.modify_static()
print("After change:", Example.static_var)

obj = Example()
print("Accessing from instance:", obj.static_var)

