'''A A A A A  
B B B B B  
C C C C C  
D D D D D  
E E E E E '''
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print(chr(65 + i), end=" ")
    print()