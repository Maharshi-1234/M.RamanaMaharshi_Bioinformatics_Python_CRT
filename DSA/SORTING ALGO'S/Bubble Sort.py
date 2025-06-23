Arr=[6,-2,0,-3,6,7]
print(f"Original Array :{Arr}" )
Count=0
for i in range(len(Arr)):
    Flag=False
    for j in range(len(Arr)-1):
        if(Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            print(Arr)
            Flag=True
    if Flag==False:
        break
print(Arr)            