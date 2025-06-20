List=[1,2,3,4,5,6,7]
sum = 0
def Add_List(List,sum):
    for i in range (len(List)):
        if bool(List[i]):
            sum=sum+List[i]
        return sum
    return Add_List(List)
print(Add_List(List,sum))

def Add_List(n,Sum):
    if bool(n):
        Sum=Sum+n
        return Sum
    return Add_List(n-1,Sum)
print(Add_List(5,0))

def summ(a,b):
    res = b
    if a!=0:
        res = res+a
        return summ(a-1,res)
    else:
        return res
print(summ(8,2))