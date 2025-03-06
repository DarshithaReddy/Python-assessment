def get_user_array():
    return list(map(int, input("Enter numbers separated by space: ").split()))
def insert_element(arr, value, position):
    arr.insert(position, value)
    return arr

arr = get_user_array()
value = int(input("Enter the value to insert: "))
position = int(input("Enter the position: "))
print("Array after insertion:", insert_element(arr, value, position))
