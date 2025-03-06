arr = [12,13,14,18,19,5,18,29]
for i in range(0,len(arr)):
    for k in range(i + 1, len(arr)):
        if arr[i] == arr[k]:
            print(arr)
            print("Duplicate element in given array is:",arr[k])
