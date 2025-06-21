st = input("Enter the name: ")
for i in range(len(st)):
    for j in range(len(st)):
        if(j==(len(st)-1)//2):
            print(st[i],end=" ")
        elif(i==(len(st)-1)//2):
            print(st[j],end=" ")
        else:
            print(" ",end=" ")
    print()