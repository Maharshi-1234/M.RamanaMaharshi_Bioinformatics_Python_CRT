#gene expression data loop thorugh the list and assign label to each number
#undrexpressed(<5),Normal(5-15),Overexpressed(>15)
n = int(input("Enter the Count of Data: "))
list=[]
list1=[]
for i in range(n):
    temp = float(input("Enter the Value: "))
    list.append(temp)
for i in list:
    