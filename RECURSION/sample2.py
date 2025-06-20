def Add_List(n,Sum):
    if bool(n):
        Sum=Sum+n
        return Sum
    return Add_List(n-1,Sum)
print(Add_List(5,5))