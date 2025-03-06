class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise MyException("This is a custom-defined exception")
except MyException as e:
    print(f"Caught MyException: {e}")
