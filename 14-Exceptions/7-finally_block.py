try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("This block always executes, regardless of an exception")
