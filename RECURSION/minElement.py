#w.a.p.p to calculate Minimum Element from the list using recursion
def find_min(lst):
    min_val = lst[0]  
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val

lst = list(map(int, input("Enter numbers: ").split()))
print("Minimum element is:", find_min(lst))
