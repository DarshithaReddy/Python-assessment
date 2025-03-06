class Example:
    static_var = "Original Value"

obj1 = Example()
obj1.static_var = "Modified in Instance"

print(Example.static_var)  # Static variable remains unchanged
print(obj1.static_var)  # Modified only for obj1

obj2 = Example()
print(obj2.static_var)  # Unchanged for new instances
