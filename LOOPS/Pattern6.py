'''
L A L A S A
L         A
L         A 
L         A
L         A
L L A L S A
'''

st = input("Enter the name: ")
for i in range(len(st)):
    for j in range(len(st)):
        if(i==0 or j==0 or j==(len(st)-1) or i==(len(st)-1)):
            print(st[j],end=" ")
        else:
            print(" ",end=" ")
    print()