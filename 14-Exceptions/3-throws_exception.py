def divide():
    raise ZeroDivisionError("Manually raised ZeroDivisionError")

try:
    divide()
except ZeroDivisionError as e:
    print(f"Caught Exception: {e}")
