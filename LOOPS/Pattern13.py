'''1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5 '''
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(1, n+1):
        print(j, end=" ")
    print()