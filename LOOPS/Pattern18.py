'''
a  
a b  
a b c  
a b c d  
a b c d e  
'''
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(chr(97 + j), end = " ")
    print()