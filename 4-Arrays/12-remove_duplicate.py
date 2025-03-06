arr = [34,45,23,78,56,45]
arr1 = []
for i in arr:
    if i not in arr1:
        arr1.append(i)
print(arr1)