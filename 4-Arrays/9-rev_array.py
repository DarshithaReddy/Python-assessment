def get_user_array():
    return list(map(int, input("Enter numbers separated by space: ").split()))

def reverse_array(arr):
    return arr[::-1]

arr = get_user_array()
print("Reversed array:", reverse_array(arr))
