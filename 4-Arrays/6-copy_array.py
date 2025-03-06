def get_array():
    return list(map(int, input("Enter numbers separated by space: ").split()))

def copy_array(arr):
    arr1 = []
    arr1 = arr.copy()
    return arr1

arr = get_array()
print("Copied array:", copy_array(arr))
