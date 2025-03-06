def get_array():
    return list(map(int, input("Enter numbers separated by space: ").split()))

def avg_array(arr):
    return sum(arr) / len(arr) 

arr = get_array()
print("Average of array:", avg_array(arr))
