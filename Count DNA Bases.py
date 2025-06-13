Str = input("Enter a Sample Base Value : ")
A,T,G,C = 0,0,0,0
count = 0
for str in Str:
    if str in 'A':
        A+=1
    elif str in 'T':
        T+=1
    elif str in 'G':
        G+=1
    else:
        C+=1
my_dict = {'A':A,'T':T,'G':G,'C':C}
print(my_dict)