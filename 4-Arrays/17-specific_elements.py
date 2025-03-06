
def get_array():
    return list(map(int, input("Enter numbers separated by space: ").split()))

def specific_array(arr):
    if 12 in arr:
        print("12 Exists in the Array")
    if 23 in arr:
        print("23 Exists in the Array")

arr = get_array()
specific_array(arr)  # No need to print, as function already prints output
