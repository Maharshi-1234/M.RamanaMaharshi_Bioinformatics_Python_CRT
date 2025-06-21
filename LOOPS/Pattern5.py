Str = "LALASA"
length=len(Str)
for i in range(length):
    for j in range(i+1):
        print(f"{Str[i]} ",end=" ")
    print()