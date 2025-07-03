'''
Problem Statement
There are three piles of stones. The first pile contains `a` stones, the second pile contains `b` stones, and the third pile contains `c` 
stones.You must choose one of the piles and split the stones from it to the other two piles. Specifically, if the chosen pile initially 
contained `s` stones,you should choose an integer `k` (0 ≤ k ≤ s), move `k` stones from the chosen pile 
onto one of the remaining two piles and `s-k` stones onto the other remaining pile.
Determine if it is possible for the two remaining piles (in any order) to contain exactly `x` and `y` stones after 
performing this action.
Input Format
The first line of the input contains a single integer `T` — the number of test cases.
The next `T` lines each contain five space-separated integers:
a b c x y
Output Format:
For each test case, print a single line 
containing `"YES"` if it is possible to obtain piles of the given sizes, or "NO" if it is impossible.
Sample Input
4
1 2 3 2 4
3 2 5 6 5
2 4 2 6 2
6 5 2 12 1
Sample Output
YES
NO
YES
YES
a,b,c = stacks
x,y = proportions to split the stacks
'''
t=int(input("Enter the integers"))
for _ in range(t):
    values = input().split()
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
    x = int(values[3])
    y = int(values[4])

    if a + b + c != x + y:
        print("NO")
    elif max(x, y) > max(a+b, b+c, c+a):
        print("NO")
    else:
        print("YES")