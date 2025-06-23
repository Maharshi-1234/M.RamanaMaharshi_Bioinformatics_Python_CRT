'''
a a a a a  
b b b b  
c c c  
d d  
e  
'''
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n - i):
        print(chr(97 + i), end=" ")
    print()