'''a b c d e  
a b c d e  
a b c d e  
a b c d e  
a b c d e '''
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print(chr(97 + j), end = " ")
    print()