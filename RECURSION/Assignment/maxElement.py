#w.a.p.p to calculate Maximum Element from the list using recursion
def find_max(lst):
    max_val = lst[0]  
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val
lst = list(map(int, input("Enter numbers: ").split()))
print("Maximum element is:", find_max(lst))