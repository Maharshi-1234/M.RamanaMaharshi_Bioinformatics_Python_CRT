st = input("Enter the name: ")
for i in range(len(st)):
    for j in range(len(st)-1,-1,-1):
        print(st[j],end="")
    print()