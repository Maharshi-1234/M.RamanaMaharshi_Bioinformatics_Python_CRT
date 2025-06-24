'''Divide and Conquer Element which selects Pivot ELement and based on that it sorts the array or elements'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len (arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
print(quick_sort([5, 3, 8, 6, 2]))