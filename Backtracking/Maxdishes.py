'''
Problem: Ramu's Buffet Choice
Ramu visits several buffet counters, each with a sequence of dishes arranged in a row. Each dish has a name 
(e.g., "Pasta", "Curry", etc.). 
He wants to eat **only one type of dish but with two restrictions:
1. He can only pick non-adjacent dishes.
2. He can only pick one type of dish throughout the buffet.
Your task is to help Ramu decide which dish type he should choose in order to maximize the number of dishes 
he can eat from a buffet, following the rules above.
If there is a tie between two or more dish types (same maximum count), Ramu will pick the dish whose name 
comes lexicographically earlier (i.e., alphabetically first).
Input Format:
The first line contains an integer `t`- the number of buffet counters Ramu visits.
For each buffet:
The first line contains an integer `n`- the number of dishes in that buffet.
The next `n` lines each contain a string -the name of a dish (e.g., `"Pasta"`, `"Curry"`).
Output Format:
For each buffet, output the name of the dish type Ramu should choose.
Constraints:
1 ≤ t ≤ 10
1 ≤ n ≤ 100
Dish names are non-empty strings of alphabets only (no special characters or numbers).
Example Input:
1
9
Pasta
Curry
Curry
Pasta
Curry
Pasta
Pasta
Pasta
Pasta
```
Example Output:
Pasta
Explanation:
Ramu can pick `Pasta` from positions: 1, 4, 7, and 9 (non-adjacent) → 4 dishes
He can pick `Curry` from positions: 2 and 5 → 2 dishes
So he chooses Pasta
'''
t=int(input("Enter the number of Buffets : "))
for _ in range(t):
    n=int(input("Enter the size of the Buffet : "))
    item=[]
    for _ in range(n):
        value=input("Enter the Dish : ")
        item.append(value)
    dish_types=set(item)
    max_dishes=0
    result=item[0]
    for dish in dish_types:
        count=0
        i=0
        while i<n:
            if item[i]==dish:
                count+=1
                i+=2
            else:
                i+=1
        if count>max_dishes or (count==max and dish<result):
            max_dishes=count
            result=dish
    print(result)