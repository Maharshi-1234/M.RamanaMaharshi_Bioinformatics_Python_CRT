num = int(input("Enter the number: "))
k=1
for i in range(num):
    for j in range(i+1):
        print(k*k,end=" ")
        k+=1
    print()