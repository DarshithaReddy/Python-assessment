import math

try:
    result = math.exp(1000)  # Exponential function with a large argument
except OverflowError as e:
    print(e)
