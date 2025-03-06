def get_user_array():
    return list(map(int, input("Enter numbers separated by space: ").split()))


def contains_value(arr, value):
    return value in arr

arr = get_user_array()
value = int(input("Enter the value to check: "))
print("Contains value:", contains_value(arr, value))
