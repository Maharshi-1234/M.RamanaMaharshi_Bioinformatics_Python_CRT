'''Ramu has N dishes of different types arranged in a row:
A1, A2, ..., AN, where Ai denotes the type of the i-th dish.
He wants to choose as many dishes as possible from the given list, but while satisfying two conditions:
1. He can choose only one type of dish.
2. **No two chosen dishes should be adjacent to each other.
Ramu wants to know **which type of dish** he should choose from, so that he can pick the maximum number of dishes.
### Example:
Given `N = 9` and `A = [1, 2, 2, 1, 2, 1, 1, 1, 1]`
For type 1, Ramu can choose at most 4 dishes.
One of the ways to choose them is: A1, A4, A7, and A9
For type 2, he can choose at most 2 dishes.
One way is to choose A3 and A5.
So, in this case, Ramu should go for type 1, from which he can pick more dishes.
'''
t = int(input("Enter the Number of Lists: "))  # Number of test cases

for _ in range(t):
    n = int(input("Enter the Size of List: "))
    A = []
    for i in range(n):
        A.append(int(input(f"Enter value at position {i+1}: ")))
    from collections import defaultdict
    pos = defaultdict(list)
    for i, dish in enumerate(A):
        pos[dish].append(i)
    max_count = 0
    best_type = None
    for dish_type, indices in pos.items():
        count = 0
        last_index = -2  
        for idx in indices:
            if idx - last_index > 1:
                count += 1
                last_index = idx
        if count > max_count:
            max_count = count
            best_type = dish_type
    print(f"Best Dish Type to Choose: {best_type} (can choose {max_count} dishes)")
