def Selection_sort(arr):
    print("Original Array: ")
    print(arr)
    n=len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
Selection_sort([-1,3,8,6,2])
print(pow(2,3,5))