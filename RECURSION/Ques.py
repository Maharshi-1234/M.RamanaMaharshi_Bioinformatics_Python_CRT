#Write a python program to print the summation of list elements using recursion
Li = [1, 2, 3, 4, 5]
def Add_List(lst):
    # Base case: if list is empty, sum is 0
    if not lst:
        return 0
    # Recursive case: sum first element + sum of the rest
    return lst[0] + Add_List(lst[1:])
print(Add_List(Li))
