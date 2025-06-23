'''
a  
b b  
c c c  
d d d d  
e e e e e  
'''
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(97 + i), end= " ")
    print()