def get_user_array():
    return list(map(int, input("Enter numbers separated by space: ").split()))

def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)


arr = get_user_array()
print("Min:", minimum(arr))
print("Max:", maximum(arr))
