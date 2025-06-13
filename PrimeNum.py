#write a python program to check whether user given number is prime or not using functions (using return)
def PrimeorNot(Num):
    c=0
    for i in range(Num):
        if(Num%(i+1)==0):
            c+=1
    if(c==2):
        return "Prime"
    else:
        return "Not Prime"
n = int(input("Enter a integer Value : "))
print(PrimeorNot(n))