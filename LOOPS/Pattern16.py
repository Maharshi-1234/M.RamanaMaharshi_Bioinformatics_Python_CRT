'''a a a a a  
b b b b b  
c c c c c  
d d d d d  
e e e e e  '''
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print(chr(97 + i), end = " ")
    print()